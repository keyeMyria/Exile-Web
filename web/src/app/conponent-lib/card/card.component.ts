import { Component, OnInit, Input } from '@angular/core';

@Component({
    selector: 'ex-card',
    templateUrl: './card.component.html'
})
export class CardComponent implements OnInit {
    isIcon:  boolean;
    @Input('icon')
    set (value: boolean) {
        this.isIcon = value != false;
    };

    constructor() { }

    ngOnInit() {
    }

}
