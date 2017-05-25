import { Component, OnInit, ElementRef } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

declare var $: any;
declare var fetch: any;
@Component({
    selector: 'exile-app',
    templateUrl: './app.component.html'
})

export class AppComponent implements OnInit {
    constructor(private elRef: ElementRef) { }
    ngOnInit() {
        let body = document.getElementsByTagName('body')[0];
        let isWindows = navigator.platform.indexOf('Win') > -1 ? true : false;
        if (isWindows) {
            body.classList.add('perfect-scrollbar-on');
        } else {
            body.classList.add('perfect-scrollbar-off');
        }
        $.material.init();
        fetch('https://api.github.com/repos/vmg/redcarpet/issues?state=closed')
            .then(res => res.json())
            .then(data => console.log(data));
    }
}
