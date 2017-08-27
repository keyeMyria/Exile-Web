import { Component, OnInit } from '@angular/core';
import { CallService, AuthService } from 'componentex';

declare var $: any;

@Component({
    selector: 'ex-nomina',
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
    constructor(private _cs: CallService, private _as: AuthService) {
        this._cs.conf({ host: '104.236.33.228', port: '8000' });
        this._as.conf('usuarios/login/', 'usuarios/is/login/');
        // this._cs.conf({ host: 'isabela.com.co' });
    }
    ngOnInit() {
        $.material.init();
    }
}
// function classDecorator(filter: Object) {
//     console.log(filter);
//     return function <T extends { new(...args: any[]): {} }>(constructor: T) {
//         return class extends constructor {
//             newProperty = 'new property';
//             hello = filter;
//         }
//     }
// }
//
// @classDecorator('hola2')
// class Greeter {
//     property = 'property';
//     hello: string;
//     constructor(m: string) {
//         this.hello = m;
//     }
// }
//
// const noc = new Greeter('Hola mundo');
// console.log(noc);
