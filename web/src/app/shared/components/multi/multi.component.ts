import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import 'rxjs/add/operator/toPromise';
import { map, tap, catchError } from 'rxjs/operators';
import { of } from 'rxjs';
@Component({
    selector: 'ex-multi',
    templateUrl: './multi.component.html'
})
export class MultiComponent implements OnInit {
    public todos = false;
    public options = [];
    @Input() service: any;
    @Input() item: any;
    @Input() form: any;
    @Input() name: string;
    @Input() placeholder: string;
    @Input() auto = true;
    @Output() ready = new EventEmitter();
    @Output() complete = new EventEmitter();
    @Input() render = item => item.id;

    constructor() {}

    ngOnInit() {
        this.ready.emit({ ready: true });
        if (!!this.item && this.item[this.name]) {
            this.form.get(this.name).patchValue(this.item[this.name]);
        }
        if (this.auto) {
            this.filterList({});
        }
    }

    onFocus(event) {
        this.filterList({});
    }

    selectAll() {
        const all = [];
        if (!this.todos) {
            this.options.forEach(element => {
                all.push(element.id);
            });
            this.form.get(this.name).patchValue(all);
            this.todos = true;
        } else {
            this.form.get(this.name).patchValue(all);
            this.todos = false;
        }
    }

    filterList(query: object) {
        const parametros = query;
        parametros['num_page'] = 0;
        this.service.list(parametros)
            .pipe(
                map((data: any) => data),
                tap((data: any) => {
                    this.options = data.object_list;
                    const num = this.options.length;
                    if (num === 0) {
                        this.placeholder = 'No se encontraron resultados';
                    } else {
                        this.placeholder = `Se encontraron ${num} registros`;
                    }
                    this.complete.emit({ options: this.options });
                }),
                catchError(error => {
                    console.log(error)
                    return of({error})
                })
            )
            .toPromise()
            .catch(error => console.log(error));
    }
}
