import { Component, OnInit, ViewChild } from '@angular/core';
import { TableComponent } from 'componentex';
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
