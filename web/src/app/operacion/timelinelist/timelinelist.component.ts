import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { NotificacionService } from '../notificacion.service';

@Component({
    selector: 'ex-timelinelist',
    templateUrl: './timelinelist.component.html',
    styleUrls: ['./timelinelist.component.scss']
})
export class TimelinelistComponent implements OnInit {

    @Input() public fecha = new Date();
    @Output() public onSelect = new EventEmitter();

    public list: any[];
    public select: any;
    public _selected: number

    constructor(private _n: NotificacionService) { }

    public ngOnInit(): void {
        this._n.list({ /*esta_completado: false*/ }).subscribe(data => {
            const result = data.json();
            this.list = result.object_list;
            if (this.list.length > 0) {
                this.setSelect(this.list[0]);
            }
        });
    }

    private setSelect(item): void {
        this.select = item;
        this._selected = this.select.id;
        this.onSelect.emit(this.select);
    }

    get selected(): number {
        return this._selected;
    }

    set selected(id: number) {
        const item2 = this.list.find(val => val.id === id);
        if (!!item2) {
            this.setSelect(item2);
        }
    }

    public onItemClick(i): void {
        this.selected = i;
    }
}
