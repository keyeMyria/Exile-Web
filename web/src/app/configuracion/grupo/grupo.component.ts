import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../shared';
import { GrupoService } from './grupo.service';
import { EmpleadoService } from '../../usuarios/empleado/empleado.service';


@Component({
    templateUrl: './grupo.component.html'
})
export class ListGrupoComponent {

    service = this._as;
    multiselect = true;
    order = [[2, 'asc']]
    icon = 'group';
    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },

        { data: 'nombre' },
    ];


    constructor(private _as: GrupoService) { }
}


@Component({
    templateUrl: './grupo.form.html'
})
export class EditGrupoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: GrupoService, public _p: EmpleadoService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            empleados: [[], Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
        ];
    }

    nombre = item => {
        return `${item.first_name} ${item.last_name} - ${item.cargo__nombre}`;
    }

    ngOnInit() {
        this._form.setReady(true);
        this._form.successful = data => {
            this._rt.navigate(['configuracion/grupo']);
        }
    }

    completeAjax(event) {
        this._form.setReady(false);
    }
}
