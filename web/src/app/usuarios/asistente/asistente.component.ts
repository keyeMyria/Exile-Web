import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from 'componentex';
import { AsistenteService } from './asistente.service';

declare var $: any;

@Component({
    template: `<ex-form #f icon="supervisor_account" title="Asistente"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [debug]="debug"
        [renderinputs]="renderinputs"></ex-form>`
})
export class AsistenteEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._as;
    deleteable = false;
    debug = true;
    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _as: AsistenteService, private _rt: Router) {
        this.form = this._fb.group({
            email: ['', [Validators.required, Validators.email, Validators.maxLength(254)]],
            first_name: ['', [Validators.maxLength(30), Validators.required]],
            last_name: ['', [Validators.maxLength(30), Validators.required]],
            identificacion: ['', [Validators.maxLength(120), Validators.required]],
            identificacion2: ['', [Validators.maxLength(120)]],
            fecha_nacimiento: ['', Validators.required],
            direccion: ['', [Validators.maxLength(120)]],
            telefono: ['', [Validators.maxLength(15)]],
            fijo: ['', [Validators.maxLength(15)]],
            // prueba: [[]]
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col2', title: 'Correo', type: 'email', name: 'email' },
            { column: 'col1', title: 'Nombre', type: 'text', name: 'first_name' },
            { column: 'col1', title: 'Apellido', type: 'text', name: 'last_name' },
            { column: 'col2', title: 'Identificación', type: 'number', name: 'identificacion' },
            { column: 'col2', title: 'Confirmar identificación', type: 'number', name: 'identificacion2', noitem: true },
            { column: 'col1', title: 'Fecha de nacimiento', type: 'text', name: 'fecha_nacimiento', class: 'datepicker' },
            { column: 'col1', title: 'Dirección', type: 'text', name: 'direccion' },
            { column: 'col1', title: 'Celular', type: 'text', name: 'telefono' },
            { column: 'col1', title: 'Telefono', type: 'text', name: 'fijo' },
            // {
            //     column: 'col2', title: 'Prueba', type: null, name: 'prueba', isSelect: true, options: [
            //         { title: 'Option1', value: '1' },
            //         { title: 'Option2', value: '2' },
            //         { title: 'Option3', value: '3' }
            //     ]
            // }
        ]
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['usuarios/asistente']);
        }
    }
}

@Component({
    templateUrl: './list.asistente.component.html'
})
export class AsistenteListComponent {
    service = this._as;
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
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'avatar',
            render: TableComponent.renderAvatar
        },
        { data: 'username' },
        { data: 'first_name' },
        { data: 'last_name' },
        { data: 'identificacion' },
        { data: 'email' },
        { data: 'telefono' },
        { data: 'fecha_nacimiento' }
    ];

    constructor(private _as: AsistenteService) { }
}
