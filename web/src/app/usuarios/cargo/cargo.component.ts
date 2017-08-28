import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from 'componentex';
import { CargoService } from './cargo.service';

@Component({
    templateUrl: './list.cargo.component.html'
})
export class CargoListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'turned_in';
    title = 'Cargos';
    service = this._as;
    multiselect = true;
    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'nombre' },
        { data: 'fecha' }
    ]

    constructor(private _as: CargoService) { }

}

@Component({
    template: `<ex-form #f icon="turned_in" title="Cargo"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditCargoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: CargoService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['usuarios/cargo']);
        }
    }
}
