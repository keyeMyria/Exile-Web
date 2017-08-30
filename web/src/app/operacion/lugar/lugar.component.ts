import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { TableComponent } from 'componentex';
import { LugarService } from './lugar.service';
@Component({
    templateUrl: './list.lugar.component.html'
})
export class LugarListComponent implements AfterViewInit {
    service = this._s;
    multiselect = true;
    aggregable = false;
    editable = false;
    deleteable = false;
    // order = [[2, 'asc']]

    @ViewChild('table') private table: TableComponent;

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'nombre' },
        { data: 'direccion' }
    ];

    constructor(private _s: LugarService) { }

    ngAfterViewInit() {
        // this.table.success = data => console.log(data);
    }

}

import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from 'componentex';

@Component({
    template: `<ex-form #f icon="account_balance" title="Lugares de Trabajo"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs">
        </ex-form>`
})
export class LugarEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: LugarService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            latitud: ['', Validators.required],
            longitud: ['', Validators.required],
            direccion: ['', Validators.required],
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Latitud', type: 'text', name: 'latitud' },
            { column: 'col1', title: 'Telefono', type: 'text', name: 'longitud' },
            { column: 'col1', title: 'Dirección', type: 'text', name: 'direccion' },
        ];
    }

    ngOnInit() {
        this._form.back = () => {
            this._rt.navigate(['operacion/lugar']);
        }
    }

}
