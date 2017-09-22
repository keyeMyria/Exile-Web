import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from 'componentex';
import { ReportesService } from './reportes.service';

@Component({
    templateUrl: './list.reportes.component.html'
})
export class ReportesListComponent {
    service = this._s;
    multiselect = true;
    order = [[2, 'asc']]

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'nombre' },
        { data: 'descripcion' },
        { data: 'tipo__nombre' },
        { data: 'cliente__nombre' },
        { data: 'lugar__nombre' },
        {
            orderable: false,
            searchable: false,
            data: 'creatorR',
            render: data => data.nombre
        },
        { data: 'fecha' }

    ];


    constructor(private _s: ReportesService) { }

}
