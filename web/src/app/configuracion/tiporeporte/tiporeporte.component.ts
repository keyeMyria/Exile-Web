import { Component, OnInit, ViewChild } from '@angular/core';
import { TableComponent } from '../../shared';
import { TipoReporteService } from './tiporeporte.service';

@Component({
    templateUrl: './list.tiporeporte.component.html'
})
export class TipoReporteListComponent {
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

    constructor(private _s: TipoReporteService) { }

}

import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../shared';

@Component({
    template: `<ex-form #f icon="format_list_bulleted" title="Tipo de Reporte"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class TipoReporteEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TipoReporteService, private _rt: Router) {
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
            this._rt.navigate(['configuracion/tipo/reporte']);
        }
    }

}
