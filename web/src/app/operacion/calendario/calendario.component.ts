import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
    selector: 'ex-calendario',
    templateUrl: './calendario.component.html',
    styleUrls: ['./calendario.component.scss']
})
export class CalendarioComponent implements OnInit {

    constructor() { }

    ngOnInit() {
        $('#calendar').fullCalendar({
            weekends: false // will hide Saturdays and Sundays
        });
    }

}
