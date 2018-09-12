import { Component, Input } from '@angular/core';

@Component({
    selector: 'ex-card',
    templateUrl: './card.component.html'
})
export class CardComponent {
    @Input('color') color = 'purple';
    @Input('title') title: string;
    @Input('subtitle') subtitle: string;
    @Input('icon') icon: string;
    @Input('header-text') headerText = false;

    constructor() { }
}
