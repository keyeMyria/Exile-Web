import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent } from '../../lib/table/table.component';
import { AsistenteService } from '../../services/usuarios/asistente.service';
import { NotificationService } from '../../services/notification.service';

declare var $: any;
declare var window: any;

@Component({
    selector: 'ex-asistente',
    templateUrl: './asistente.component.html'
})
export class AsistenteComponent implements OnInit {

    constructor(private _as: AsistenteService, private _ns: NotificationService) { }

    ngOnInit() {}
}

@Component({
    selector: 'ex-asistente-edit',
    templateUrl: './edit.asistente.component.html'
})
export class AsistenteEditComponent implements OnInit {

    form: FormGroup;

    constructor(private _fb: FormBuilder) {
        this.form = this._fb.group({
            username: ['', Validators.required],
            password1: ['', Validators.required],
            password2: ['', Validators.required],
            email: ['', Validators.required],
            first_name: ['', Validators.required],
            last_name: ['', Validators.required],
            identificacion: ['', Validators.required],
            fecha_nacimiento: ['', Validators.required],
            direccion: ['', Validators.required],
            telefono: ['', Validators.required],
            fijo: ['', Validators.required],
            imagen: ['', Validators.required]
        });
        this.form.valueChanges.subscribe(val => {
            console.log('cambio a: ', val);
        });
    }

    ngOnInit() {}

    isValid(): boolean {
        return this.form.valid;
    }

    fileChange($event) {
        // this.values = this.form.value;
        // this.values['imagen2'] = $event.target.files[0];
        // console.log(this.values['imagen2']);
        // window.noc = $event;
        // this.form.value.append({image2: $event.target.files[0]});
    }

    getValues(): any {
    }

    save() {
        console.log('save');
    }
}

@Component({
    selector: 'ex-asistente-list',
    templateUrl: './list.asistente.component.html'
})
export class AsistenteListComponent implements OnInit {

    @ViewChild('table') private table: TableComponent;

    constructor(private _as: AsistenteService) {  }

    onChange($event) {
        console.log($event);
    }

    ngOnInit() {
        this.table.multiSelectable = true;
        this.table.columns = [
            {
                className: 'text-center',
                orderable: false,
                searchable: false,
                data: 'id',
                render: this.table.renderCheckRow
            },
            { data: 'username' },
            {
                data: 'nombre',
                render: (data, type, full, meta) => {
                    return `${data.first_name} ${data.last_name}`;
                }
            },
            { data: 'identificacion' },
            { data: 'email' },
            { data: 'telefono' },
            {
                className: 'ex-table-btn',
                orderable: false,
                searchable: false,
                data: 'id'
            },
        ];

        this.table.preAjax = data => {
            if (data.sort_property === 'nombre') {
                data.sort_property = 'first_name';
            }
            return data;
        };

        this.table.service = this._as;
    }

}
