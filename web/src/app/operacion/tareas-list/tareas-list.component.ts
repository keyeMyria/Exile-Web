import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { TableComponent } from 'componentex';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from 'componentex';
import { TareaService } from '../tarea/tarea.service';

@Component({
    templateUrl: './list.tareas-list.component.html'
})
export class TareaListComponent implements OnInit {
    service = this._s;
    multiselect = true;
    aggregable = false;
    editable = false;
    deleteable = false;
    order = [[2, 'asc']]

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
        {
            orderable: false,
            searchable: false,
            data: 'creator',
            render: data => data.username
        },
        { data: 'fecha_ejecucion' }
    ];


    constructor(private _s: TareaService) { }

    ngOnInit() {
        this.table.success = data => {
            console.log(data);
        }
    }
}


import { ClienteService } from '../cliente/cliente.service';
import { LugarService } from '../lugar/lugar.service';
import { GrupoService } from '../../configuracion/grupo/grupo.service';
import { EmpleadoService } from '../../usuarios/empleado/empleado.service';

@Component({
    templateUrl: './form.tarea-list.component.html',
    styleUrls: ['./tareas-list0.component.scss']
})
export class TareaFormComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[]; i
    service = this._s;
    debug = true;
    // item: any;
    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TareaService, private _rt: Router, private _ar: ActivatedRoute,
        public _c: ClienteService, public _l: LugarService, public _g: GrupoService, public _p: EmpleadoService) {

        this.form = this._fb.group({
            nombre: ['', [Validators.required, Validators.maxLength(100)]],
            descripcion: ['', [Validators.required, Validators.maxLength(400)]],
            latitud: ['', []],
            longitud: ['', []],
            lugar: ['', []],
            cliente: ['', []],
            empleados: ['', []],
            grupo: ['', []],
            fecha_ejecucion: ['', []],
            fecha_finalizacion: ['', []],
            period: ['', []],
            every: ['', [Validators.min(0)]]
        });
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition((position) => {
                this.form.get('latitud').setValue(position.coords.latitude);
                this.form.get('longitud').setValue(position.coords.longitude);
            });
        }
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Descripción', type: 'textarea', name: 'descripcion' },
            { column: 'col2', title: 'Fecha de Ejecucion', type: 'text', name: 'fecha_ejecucion', class: 'datetimepicker' },
            { column: 'col2', title: 'Fecha de Finalizacion', type: 'text', name: 'fecha_finalizacion', class: 'datetimepicker' },
            {
                column: 'col2', title: 'Periodo', isSelect: true, name: 'period', type: 'select', options: [
                    { title: '-----', value: null },
                    { title: 'Dias', value: 'days' },
                    { title: 'Horas', value: 'hours' },
                    { title: 'Minutos', value: 'minutes' },
                    { title: 'Segundos', value: 'seconds' },
                    { title: 'Microsegundos', value: 'microseconds' }
                ]
            },
            { column: 'col2', title: 'Frecuencia', type: 'number', name: 'every' }
        ];
        // if (!!this._ar.snapshot.data['item'] && Object.keys(this._ar.snapshot.data['item']).length !== 0) {
        //     this.item = this._ar.snapshot.data['item'];
        // }

    }


    itemCliente = data => {
        return data.cliente__nombre
    };
    itemLugar = data => {
        return data.lugar__nombre
    };
    itemGrupo = data => {
        return data.grupo.nombre
    };
    itemEmpleado = data => {
        return `${data.first_name} ${data.last_name}`
    }

    ngAfterViewInit() {
        this._form.back = () => {
            this._rt.navigate(['operacion/tarea'])
        }
    }

    completeAjax(event) {
        // console.log(event)
    }
}
