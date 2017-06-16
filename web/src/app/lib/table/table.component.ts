import { Component, OnInit, Input, ElementRef, ViewChild } from '@angular/core';
import { NotificationService } from '../../services/notification.service';
declare var $: any;

@Component({
    selector: 'ex-table',
    templateUrl: './table.component.html',
})
export class TableComponent implements OnInit {

    @ViewChild('table') private table: ElementRef;

    private dataTable: any;
    public service: any;
    public columns: any[] = [];
    public columnDefs: any[] = [];
    public conf: any;
    public selectedItems: any[] = [];
    public multiSelectable = false;

    constructor(private _ns: NotificationService) {  }

    ngOnInit() {
        const table = this.table.nativeElement;
        this.conf = {
            processing: true,
            serverSide: true,
            pagingType: 'full_numbers',
            responsive: true,
            ajax: (data, callback, settings) => {
                const op = {
                    page: Math.ceil(data.start / data.length) + 1,
                    num_page: data.length,
                    sort_property: this.columns[data.order[0].column].data,
                    sort_direction: data.order[0].dir,
                    q: data.search.value
                };
                this.ajax(data.draw, op, callback);
            },
            columns: this.columns,
            language: {
                sProcessing: `
                    <div class="loader">
                        <svg class="circular" viewBox="25 25 50 50">
                            <circle class="path" cx="50" cy="50" r="20" fill="none" stroke-width="2" stroke-miterlimit="10"/>
                        </svg>
                    </div>`,
                sLengthMenu: 'Mostrar _MENU_ registros',
                sZeroRecords: 'No se encontraron resultados',
                sEmptyTable: 'Ningun dato disponible',
                sInfo: 'Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros',
                sInfoEmpty: 'Ningun dato disponible',
                sInfoFiltered: '(filtrado de un total de _MAX_ registros)',
                sInfoPostFix: '',
                sSearch: 'Buscar:',
                sUrl: '',
                sInfoThousands: ',',
                sLoadingRecords: 'Cargando...',
                oPaginate: {
                    sFirst: 'Primero',
                    sLast: 'Ultimo',
                    sNext: 'Siguiente',
                    sPrevious: 'Anterior'
                },
                oAria: {
                    sSortAscending: ': Activar para ordenar la columna de manera ascendente',
                    sSortDescending: ': Activar para ordenar la columna de manera descendente'
                }
            }
        };
        this.dataTable = $(table).DataTable(this.conf);
        this._selectionInit(table);
    }

    _selectionInit(table) {
        if (this.multiSelectable) {
            const self = this;
            $(table).on('click', 'tbody tr', function(event){
                self._onSelectedRow(this);
                event.preventDefault();
            });
            // $(table).on('change', 'tbody tr td input[type=checkbox][name=selectedItems]', function(){
            //     if ($(this).is(':checked')) {
            //         console.log('check');
            //         // self._onSelectedRow(this);
            //     }
            // });
        }
    }

    _onSelectedRow(tr) {
        const self = this;
        const table = this.table.nativeElement;
        const check = $(tr).find('input[type=checkbox][name=selectedItems]');
        $(tr).toggleClass('selected');
        check.prop('checked', !check.is(':checked'));
        this.selectedItems = [];
        $.each($(table).find('tr.selected'), function() {
            self.selectedItems.push(self.dataTable.row(this).data());
        });
    }

    preAjax(data) {
        return data;
    }

    ajax(draw: number, dataSource: any, cb: any): void {
        dataSource = this.preAjax(dataSource);
        this.service.list(dataSource)
            .then(res => res.json())
            .then(data => {
                console.log('res');
                cb({ 'draw': draw, 'recordsTotal': data.count, 'recordsFiltered': data.num_rows, 'data': data.object_list });
            })
            .catch(err => {
                cb({ 'recordsTotal': 0, 'recordsFiltered': 0, 'data': [] });
                this._ns.error('Ha ocurrido un error al consultar los datos');
            });
    }

    renderCheckRow(data, type, full, meta) {
        return `
        <div class="checkbox">
            <label><input type="checkbox" name="selectedItems" value="${data}"/></label>
        </div>`;
    }
}
