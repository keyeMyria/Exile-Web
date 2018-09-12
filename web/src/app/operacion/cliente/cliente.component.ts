import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { TableComponent } from '../../shared';
import { ClienteService } from './cliente.service';
import { TipoclienteService } from '../../configuracion/tipocliente/tipocliente.service';

@Component({
    templateUrl: './list.cliente.component.html'
})
export class ClienteListComponent implements AfterViewInit {
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
        { data: 'identificacion' },
        { data: 'tipo__nombre' },
        { data: 'telefono' },
        { data: 'direccion' }
    ];

    constructor(private _s: ClienteService) { }

    ngAfterViewInit() {
        // this.table.success = data => console.log(data);
    }

}

import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../shared';

@Component({
    template: `<ex-form #f icon="account_box" title="Cliente"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs">
            <div top-form class="row">
                <div class="col-lg-12">
                    <div class="form-horizontal">
                        <div class="row">
                            <label class="col-lg-3 label-on-left" for="id_cargo">Tipo de Cliente:</label>
                            <div class="col-lg-9">
                                <div class="form-group label-floating is-empty">
                                    <label class="control-label"></label>
                                    <ex-autocomplete name="tipo" [service]="_c" [form]="form"
                                        [item]="_form.item" [itemVal]="itemTipo"></ex-autocomplete>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </ex-form>`
})
export class ClienteEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: ClienteService, private _rt: Router, public _c: TipoclienteService) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            identificacion: ['', Validators.required],
            tipo: ['', Validators.required],
            telefono: ['', Validators.required],
            direccion: ['', Validators.required],
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Identificación', type: 'text', name: 'identificacion' },
            { column: 'col1', title: 'Telefono', type: 'text', name: 'telefono' },
            { column: 'col1', title: 'Dirección', type: 'text', name: 'direccion' },
        ];
    }

    /**
    *nnoc hola munco
    */
    ngOnInit() {
        this._form.back = () => {
            this._rt.navigate(['operacion/cliente']);
        }
    }

    itemTipo = data => data.nombre;

}
