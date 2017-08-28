import { Component, OnInit, ViewChild } from '@angular/core';
import { TableComponent } from 'componentex';
import { TipoclienteService } from './tipocliente.service';

@Component({
    templateUrl: './list.tipocliente.component.html'
})
export class TipoclienteListComponent implements OnInit {
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

    ngOnInit() {

    }
}
