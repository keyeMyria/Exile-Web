import { Component, OnInit, ViewChild } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent, ExgmapComponent } from 'componentex';
import { ReportesService } from './reportes.service';
import { TipoReporteService } from '../../configuracion/tiporeporte/tiporeporte.service';
import { ClienteService } from '../../operacion/cliente/cliente.service';
import { LugarService } from '../../operacion/lugar/lugar.service';

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
            data: 'creator',
            render: data => `${data.first_name} ${data.last_name}`
        },
        { data: 'fecha' }

    ];


    constructor(private _s: ReportesService) { }

}


@Component({
    templateUrl: './reporte.form.html'
})
export class EditReporteComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;
    @ViewChild('map') private map: ExgmapComponent;

    constructor(private _fb: FormBuilder, private _s: ReportesService, public _t: TipoReporteService, public _l: LugarService, public _c: ClienteService, private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            nombre: ['', [Validators.required]],
            descripcion: ['', [Validators.required]],
            tipo: [[],],
            cliente: [[],],
            lugar: [[],],
            latitud: ['',],
            longitud: ['',],
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Descripción', type: 'text', name: 'descripcion' },

        ];
    }

    itemTipo = item => item.tipo__nombre;
    itemCliente = item => item.cliente__nombre;
    itemLugar = item => item.lugar__nombre;

    ngOnInit() {
        this._form.preSave = data => {
            data['fotoreporte_set-TOTAL_FORMS'] = 0;
            data['fotoreporte_set-INITIAL_FORMS'] = 0;
            data['fotoreporte_set-MAX_NUM_FORMS'] = 1000;
            data['fotoreporte_set-MIN_NUM_FORMS'] = 0;
            return data;
        }
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.map.currentPosition = false;
            this.map.coords = { lat: this._r.snapshot.data['item'].latitud, lng: this._r.snapshot.data['item'].longitud }
            this.map.zoom = 16;
        }
        this._form.successful = data => {
            this._rt.navigate(['novedades/reportes']);
        }
    }

    onCoordsChange(event) {
        this.form.get('latitud').setValue(event.lat);
        this.form.get('longitud').setValue(event.lng);
    }
}
