import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { TableComponent } from 'componentex';
import { LugarService } from './lugar.service';
@Component({
    templateUrl: './list.lugar.component.html'
})
export class LugarListComponent implements AfterViewInit {
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
        { data: 'direccion' }
    ];

    constructor(private _s: LugarService) { }

    ngAfterViewInit() {
        // this.table.success = data => console.log(data);
    }

}

import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent, ExgmapComponent } from 'componentex';

@Component({
    template: `
    <ex-form #f icon="account_balance" title="Lugares de Trabajo"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs">
        <div bottom-form class="row">
            <div class="col-lg-12">
                <div class="form-horizontal">
                    <div class="row">
                        <label class="col-lg-3 label-on-left" for="id_cargo">Ubicación</label>
                        <div class="col-lg-9">
                            <div class="form-group label-floating is-empty">
                                <ex-gmap #map (coordsChange)="onCoordsChange($event)"></ex-gmap>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </ex-form>`
})
export class LugarEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    latitude: number;
    longitude: number;

    @ViewChild('f') private _form: FormComponent;
    @ViewChild('map') private map: ExgmapComponent;

    constructor(private _fb: FormBuilder, private _s: LugarService, private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            latitud: ['', Validators.required],
            longitud: ['', Validators.required],
            direccion: ['', Validators.required],
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Dirección', type: 'text', name: 'direccion' },
        ];

    }

    ngOnInit() {
        this._form.back = () => {
            this._rt.navigate(['operacion/lugar']);
        }
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.map.currentPosition = false;
            this.map.coords = { lat: this._r.snapshot.data['item'].latitud, lng: this._r.snapshot.data['item'].longitud }
            this.map.zoom = 16;
        }
    }

    onCoordsChange(event) {
        this.form.get('latitud').setValue(event.lat);
        this.form.get('longitud').setValue(event.lng);
    }

    onItemChange(event) {

        console.log(this.map.coords)
    }
}
