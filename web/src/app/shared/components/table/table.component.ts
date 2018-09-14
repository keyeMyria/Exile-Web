import { Component, OnInit, Input, ElementRef, ViewChild, Output, EventEmitter  } from '@angular/core';
import { BsNotify } from '../../utils/bs.notify';
import { CallService } from '../../services/call.service';

declare var $: any;
declare var window: any;
declare var swal: any;

@Component({
    selector: 'ex-table',
    templateUrl: './table.component.html'
})
export class TableComponent implements OnInit {

    @ViewChild('table') public table: ElementRef;

    @Input() public icon: string;
    @Input() public title: string;
    @Input() public service: any;
    @Input() public columns: any[] = [{ data: 'id' }];
    @Input() public multiselect = false;
    @Input() public deleteable = true;
    @Input() public aggregable = true;
    @Input() public editable = true;
    @Input() public order: any[] = [[1, 'asc']];
    @Input() public addlink = [0, 'edit'];
    @Input() public enable = true;
    public dataTable: any;
    public selectedItems: any[] = [];

    @Output() selectedItemsChange = new EventEmitter();

    public static renderCheckRow(data) {
        return `
        <div class="checkbox">
            <label><input type="checkbox" name="selectedItems" value="${data}"/></label>
        </div>`;
    }

    public static renderDecimal(data) {
        return parseFloat(data).toFixed(2);
    }

    public static renderAvatar(data) {
        if (!data) {
            data = '/assets/img/default-avatar.png';
        } else {
            data = `${window._server}${data}`
        }
        return `<div class="avatar" style="background-image: url(${data});"></div>`;
    }

    constructor(public _cs: CallService) { }

    get itemSelected(): any {
        return this.selectedItems[0] ? this.selectedItems[0] : null;
    }
    ngOnInit() {
        const table = this.table.nativeElement;
        const conf = {
            processing: true,
            serverSide: true,
            pagingType: 'full_numbers',
            responsive: true,
            order: this.order,
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
            },
            drawCallback: (settings) => {
                this.drawCallback();
                this._selectionInit(table);
            }
        };
        if (this.enable) {
            this.dataTable = $(table).DataTable(conf);
        }
    }
    drawCallback() { }
    _selectionInit(table) {
        if (this.multiselect) {
            const self = this;
            $(table).find('tbody tr input[type=checkbox][name=selectedItems]').on('change', function(event) {
                self._onSelectedRow($(this).closest('tr')[0]);
            });
            $('#selectAll').on('change', function(event) {
                const check = this.checked;
                $.each($(table).find('tbody tr input[type=checkbox][name=selectedItems]'), function(id, val) {
                    const tr = $(val).closest('tr')[0];
                    if (check !== val.checked) {
                        $(val).prop({ checked: check });
                        self._onSelectedRow(tr);
                    }
                });
            });
        }
    }

    _onSelectedRow(tr) {
        const self = this;
        const table = this.table.nativeElement;
        $(tr).toggleClass('selected');
        this.selectedItems = [];
        $.each($(table).find('tr.selected'), function() {
            self.selectedItems.push(self.dataTable.row(this).data());
        });
        this.selectedItemsChange.emit({ selectedItems: this.selectedItems });
    }


    preAjax(data) {
        return data;
    }

    ajax(draw: number, dataSource: any, cb: any): void {
        if (this.service) {
            dataSource = this.preAjax(dataSource);
            this.service.list(dataSource)
                .subscribe(
                    res => {
                        const data = res;
                        this.selectedItems = [];
                        this.selectedItemsChange.emit({ selectedItems: this.selectedItems });
                        this.service.data = data.object_list;
                        this.success(this.service.data);
                        cb({ 'draw': draw, 'recordsTotal': data.count, 'recordsFiltered': data.count, 'data': data.object_list });
                    },
                    err => {
                        cb({ 'recordsTotal': 0, 'recordsFiltered': 0, 'data': [] });
                        BsNotify.error('Ha ocurrido un error al consultar los datos');
                    }
                );
        } else {
            cb({ 'recordsTotal': 0, 'recordsFiltered': 0, 'data': [] });
            BsNotify.error('No has definido un servicio que consultar');
        }
    }


    success(data: any) { }

    onDelete() {
        if (this.deleteable) {
            swal({
                title: 'Estás seguro? ',
                text: `Se eliminarán ${this.selectedItems.length} registro(s).`,
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#213b78',
                cancelButtonColor: '#ff9800',
                cancelButtonText: 'Cancelar',
                confirmButtonText: 'Eliminar'
            }).then(() => {
                const deletedList = [];
                for (const item of this.selectedItems) {
                    deletedList.push(this.service.delete(item.id).toPromise())
                }
                Promise.all(deletedList)
                    .then(data => {
                        this.dataTable.ajax.reload();
                        swal({
                            title: 'Eliminado!',
                            text: 'Todos los registros se eliminaron con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                    })
                    .catch(err => {
                        this.dataTable.ajax.reload();
                        BsNotify.error('No se han podido eliminar los registros');
                        console.error(err);
                    })
            }, () => { });
        }
    }

    get editlink() {
        return this._editlink();
    }

    _editlink: any = () => {
        const aux = this.itemSelected;
        if (!!aux) {
            return [aux.id, 'edit']
        }
        return [aux]
    }

    set editlink(fn) {
        this._editlink = fn;
    }
}
