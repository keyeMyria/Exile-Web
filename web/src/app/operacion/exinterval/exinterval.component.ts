import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
@Component({
    selector: 'ex-interval',
    templateUrl: './exinterval.component.html',
    styleUrls: ['./exinterval.component.scss']
})
export class ExintervalComponent implements OnInit {

    public options = [
        { title: '-----', value: '----' },
        { title: 'Dias', value: 'days' },
        { title: 'Horas', value: 'hours' },
        { title: 'Minutos', value: 'minutes' },
        { title: 'Segundos', value: 'seconds' },
        { title: 'Microsegundos', value: 'microseconds' }
    ]

    public selectedValue = '----';
    public selectedMes: string;
    public selectedIntervalo: string;

    constructor() { }

    ngOnInit() {
    }

}
