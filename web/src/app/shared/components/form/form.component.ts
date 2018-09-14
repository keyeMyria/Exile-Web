import { Component, Input, Output, OnInit, AfterViewInit, EventEmitter } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { BsNotify } from '../../utils';
import 'rxjs/add/operator/toPromise';
import { map, tap, flatMap, first, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

declare var $: any;
declare var swal: any;

export interface SelectInput {
    title: string;
    value: any;
}

export const DATE_TIME = 'MM/DD/YYYY h:mm A';
export const DATE = 'MM/DD/YYYY';
export const TIME = 'h:mm A';

export interface RenderInput {
    column: string;
    title: string;
    type: string;
    name: string;
    isSelect?: boolean;
    multiple?: boolean;
    disabled?: boolean;
    step?: string;
    options?: SelectInput[];
    class?: string;
    error?: string;
    noitem?: boolean;
}

@Component({
    selector: 'ex-form',
    templateUrl: './form.component.html'
})
export class FormComponent implements OnInit, AfterViewInit {

    @Input() public title: string;
    @Input() public icon: string;
    @Input() public columns: string[];
    @Input() public renderinputs: RenderInput[];
    @Input() public form: FormGroup;
    @Input() public service: any;
    @Input() public deleteable = true;
    @Input() public saveable = true;
    @Input() public otro = true;
    @Input() public debug = false;
    @Input() public retur = true;
    @Output() public itemChange = new EventEmitter();
    public _ready: boolean;
    public item: any;

    private errorMessages = {
        email: 'Ingrese una dirección de correo valida',
        required: 'Este campo es requerido',
        url: 'Ingrese una url',
        min: data => {
            return `El valor debe ser mayor o igual a ${data.min}, actualmente es ${data.actual}`;
        },
        max: data => {
            return `El valor debe ser menor o igual a ${data.max}, actualmente es ${data.actual}`;
        },
        minlength: data => {
            return `El numero de caracteres debe ser mayor o igual a ${data.requiredLength}, actualmente es ${data.actualLength}`;
        },
        maxlength: data => {
            return `El numero de caracteres debe ser menor o igual a ${data.requiredLength}, actualmente es ${data.actualLength}`;
        },
    };

    constructor(private _ar: ActivatedRoute) { }

    setReady(val: boolean) {
        this._ready = val;
    }

    setItem(item: any) {
        item = this.prePatchValue(item);
        if (item) {
            this.item = item;
            this.form.patchValue(this.item);
        }
        this.itemChange.emit(this.item);
    }

    prePatchValue(value) {
        return value;
    }

    ngOnInit() {
        if (!!this._ar.snapshot.data['item'] && Object.keys(this._ar.snapshot.data['item']).length !== 0) {
            this.setItem(this._ar.snapshot.data['item']);
        }
        this.form.valueChanges.subscribe(data => this.onValueChanged(data));
    }

    ngAfterViewInit() {
        const self = this;
        // format: 'H:mm', use this format if you want the 24hours timepicker
        // format: 'h:mm A' use this format if you want the 12hours timpiecker with AM/PM toggle
        const dt = DATE_TIME;
        const d = DATE;
        const t = TIME;
        const op = {
            time: 'fa fa-clock-o',
            date: 'fa fa-calendar',
            up: 'fa fa-chevron-up',
            down: 'fa fa-chevron-down',
            previous: 'fa fa-chevron-left',
            next: 'fa fa-chevron-right',
            today: 'fa fa-screenshot',
            clear: 'fa fa-trash',
            close: 'fa fa-remove',
            inline: true
        };
        $('.datetimepicker').datetimepicker({ format: dt, icons: op });
        $('.datepicker').datetimepicker({ format: d, icons: op });
        $('.timepicker').datetimepicker({ format: 'h:mm A', icons: op });
        $('.datetimepicker').on('dp.change', function(e) {
            self.form.get($(this).attr('name')).setValue($(this).datetimepicker({ format: dt }).val());
        });
        $('.datepicker').on('dp.change', function(e) {
            self.form.get($(this).attr('name')).setValue($(this).datetimepicker({ format: d }).val());
        });
        $('.timepicker').on('dp.change', function(e) {
            self.form.get($(this).attr('name')).setValue($(this).datetimepicker({ format: t }).val());
        });
    }

    onValueChanged(data) {
        if (!this.form) { return; }
        for (const input of this.renderinputs) {
            input.error = (() => {
                const control = this.form.get(input.name);
                if (control && control.dirty && !control.valid) {
                    let res = '';
                    for (const key in control.errors) {
                        if (!!control.errors[key]) {
                            let messege = '';
                            const errors = this.errorMessages[key];
                            if (typeof errors === 'function') {
                                messege = errors(control.errors[key]);
                            } else {
                                messege = errors;
                            }
                            res += messege || key + ' ';
                        }
                    }
                    return res;
                }
                return null;
            })();
        }
    }

    isValid(): boolean {
        return this.form.valid;
    }

    isRender(col1, col2, item): boolean {
        if (item) {
            return col1 === col2 && !this.item;
        } else {
            return col1 === col2;
        }
    }

    save(back?: boolean) {
        if (!!this.service && this.form.valid) {
            const body = this.preSave(this.form.value);
            this._ready = true;
            if (!!this.item) {
                this.service.edit(this.item.id, body)
                    .toPromise()
                    .then(data => {
                        this._ready = false;
                        this.successful(data);
                        this.back();
                        swal({
                            title: 'Guardado!',
                            text: 'Registro se guardo con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                    })
                    .catch(error => this._error(error, 'Ha ocurrido un error al intentar guardar los datos'));


            } else {
                this.service.add(body)
                    .toPromise()
                    .then(data => {
                        this.form.reset();
                        this._ready = false;
                        swal({
                            title: 'Guardado!',
                            text: 'Registro se guardo con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                        this.successful(data);
                        if (!back) {
                            this.back();
                        }
                    })
                    .catch(error => this._error(error, 'Ha ocurrido un error al intentar gurdar los datos'))
            }
        } else {
            console.error('no se ha definido un service para este formulario');
        }
    }

    _findErros(errs) {
        if (errs) {
            for (const input of this.renderinputs) {
                input.error = (() => {
                    for (const key in errs) {
                        if (!!errs[key] && input.name === key) {
                            return errs[key];
                        }
                    }
                    return null;
                })();
            }
        }

    }

    delete() {
        if (!!this.service && !!this.item && this.deleteable) {
            swal({
                title: 'Está seguro?',
                text: 'Se eliminará 1 registro.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#213b78',
                cancelButtonColor: '#ff9800',
                cancelButtonText: 'Cancelar',
                confirmButtonText: 'Eliminar'
            }).then(() => {
                this.service.delete(this.item.id)
                    .toPromise()
                    .then(data => {
                        this.successful(data);
                        this.back();
                        swal({
                            title: 'Eliminado!',
                            text: 'Registros se eliminado con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                    })
                    .catch(error => this._error(error, 'No se han podido eliminar los registros'));
            }, () => { });
        }
    }

    preSave(body): any {
        return body;
    }

    successful(data) { }

    back() {
        this.successful(null);
    }

    error(error) { }

    _error(error: any, defaultMgs: string) {
        this._ready = false;
        console.log(error);
        switch (error.status) {
            case 0:
                console.log(error);
                swal({
                    title: 'Sin Conexión!',
                    text: 'Verifique su Conexión a Internet.',
                    type: 'warning',
                    confirmButtonColor: '#213b78',
                });
                break;
            case 400:
                this.error(error);
                this._findErros(error.json());
                break;
            case 403:
                swal({
                    title: 'Sin Acceso!',
                    text: 'Usted no tiene permitido realizar este cambio.',
                    type: 'warning',
                    confirmButtonColor: '#213b78',
                });
                break;
            case 404:
                swal({
                    title: 'No se pudo encontrar el objeto!',
                    // text: 'Usted no tiene permitido realizar este cambio.',
                    type: 'warning',
                    confirmButtonColor: '#213b78',
                });
                break;
            case 408:
                swal({
                    title: 'Su solicitud ha tardado mucho tiempo!',
                    text: 'Por favor verifique su Conexión a Internet y vuelva a intentarlo.',
                    type: 'warning',
                    confirmButtonColor: '#213b78',
                });
                break;
            default:
                this.error(error);
                BsNotify.error(defaultMgs);
                // console.error(error.json());
                break;
        }
    }
}
