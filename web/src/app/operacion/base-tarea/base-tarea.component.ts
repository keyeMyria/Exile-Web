import { Component, ViewChild, OnInit, ElementRef, AfterViewInit } from '@angular/core';
import { MdSidenav } from '@angular/material';
import { Router, NavigationEnd } from '@angular/router';
// import { AuthService } from '../../services/auth.service'
import 'rxjs/add/operator/filter';

declare var $: any;

@Component({
    selector: 'ex-base-tarea',
    templateUrl: './base-tarea.component.html',
    styleUrls: ['./base-tarea.component.scss']
})
export class BaseComponent implements OnInit, AfterViewInit {

    @ViewChild('sidenav') sidenav: MdSidenav;

    constructor(private router: Router) { }

    ngAfterViewInit() {
        this.router.events
            .filter(event => event instanceof NavigationEnd)
            .subscribe((event: NavigationEnd) => {
                if (this.sidenav.mode === 'over') {
                    this.sidenav.close();
                }
            });
    }

    ngOnInit() {
        this.initSidenav(window.innerWidth)
        $(document.body).addClass('nav-open');
    }

    onResize(event) {
        this.initSidenav(event.target.innerWidth);
    }

    private initSidenav(width: number) {
        if (width < 991) {
            if (this.sidenav.mode !== 'over') {
                this.sidenav.close();
                this.sidenav.mode = 'over'
            }
        } else {
            if (this.sidenav.mode !== 'side') {
                this.sidenav.open();
                this.sidenav.mode = 'side'
            }
        }
    }
}
