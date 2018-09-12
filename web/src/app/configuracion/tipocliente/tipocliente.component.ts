import { Component, OnInit, ViewChild } from '@angular/core';
import { TableComponent } from '../../shared';
import { TipoclienteService } from './tipocliente.service';

@Component({
    templateUrl: './list.tipocliente.component.html'
})
export class TipoclienteListComponent {
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
        { data: 'nombre' }
    ];

    constructor(private _s: TipoclienteService) { }

}

import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../shared';

@Component({
    template: `<ex-form #f icon="format_list_bulleted" title="Tipo de Cliente"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class TipoclienteEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TipoclienteService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
        ];
    }

    ngOnInit() {
        this._form.back = () => {
            this._rt.navigate(['configuracion/tipo/cliente']);
        }
    }

}
