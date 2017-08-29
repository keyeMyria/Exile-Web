import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from 'componentex';
import { EmpleadoService } from './empleado.service';


@Component({
    template: `<ex-form #f icon="account_circle" title="Empleador"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditEmpleadoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._as;


    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _as: EmpleadoService, private _rt: Router) {
        this.form = this._fb.group({
            username: ['', [Validators.required, Validators.maxLength(150)]],
            password1: ['', [/*Validators.required*/]],
            password2: ['', [/*Validators.required*/]],
            email: ['', [Validators.required, Validators.email, Validators.maxLength(254)]],
            first_name: ['', [Validators.maxLength(30), Validators.required]],
            last_name: ['', [Validators.maxLength(30), Validators.required]],
            identificacion: ['', [Validators.maxLength(120), Validators.required]],
            fecha_nacimiento: ['', Validators.required],
            fecha_ingreso: ['',],
            fecha_retiro: ['',],
            direccion: ['', [Validators.maxLength(120)]],
            telefono: ['', [Validators.maxLength(15)]],
            fijo: ['', [Validators.maxLength(15)]]
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col2', title: 'Nombre de Usuario', type: 'text', name: 'username' },
            { column: 'col2', title: 'Contraseña', type: 'password', name: 'password1', noitem: true },
            { column: 'col2', title: 'Confirmar contraseña', type: 'password', name: 'password2', noitem: true },
            { column: 'col2', title: 'Correo', type: 'email', name: 'email' },
            { column: 'col1', title: 'Nombre', type: 'text', name: 'first_name' },
            { column: 'col1', title: 'Apellido', type: 'text', name: 'last_name' },
            { column: 'col1', title: 'Identificación', type: 'text', name: 'identificacion' },
            { column: 'col1', title: 'Fecha de nacimiento', type: 'text', name: 'fecha_nacimiento', class: 'datepicker' },
            { column: 'col1', title: 'Fecha de ingreso', type: 'text', name: 'fecha_ingreso', class: 'datepicker' },
            { column: 'col1', title: 'Fecha de retiro', type: 'text', name: 'fecha_retiro', class: 'datepicker' },
            { column: 'col1', title: 'Dirección', type: 'text', name: 'direccion' },
            { column: 'col1', title: 'Celular', type: 'text', name: 'telefono' },
            { column: 'col1', title: 'Telefono', type: 'text', name: 'fijo' }
        ]

    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['usuarios/empleado']);
        }
    }
}

@Component({
    templateUrl: './list.empleado.component.html'
})
export class ListEmpleadoComponent {

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
        { data: 'cargo__nombre' },
        { data: 'email' },
        { data: 'telefono' },
        { data: 'fijo' },
        { data: 'fecha_ingreso' },
        { data: 'fecha_retiro' },
    ];


    constructor(private _as: EmpleadoService) { }
}
