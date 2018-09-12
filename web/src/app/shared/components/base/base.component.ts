import { Component, ViewChild, OnInit, ElementRef, AfterViewInit } from '@angular/core';
import { MatSidenav } from '@angular/material';
import { Router, NavigationEnd } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { filter } from 'rxjs/operators';

declare var $: any;

@Component({
    templateUrl: './base.component.html',
    styleUrls: ['./base.component.scss']
})
export class BaseComponent implements OnInit, AfterViewInit {

    @ViewChild('sidenav') sidenav: MatSidenav;

    constructor(private router: Router, private _s: AuthService) { }

    ngAfterViewInit() {
        this.router.events
            .pipe(
                filter(event => event instanceof NavigationEnd)
            ).subscribe((event: NavigationEnd) => {
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

    onLogout() {
        this._s.logout();
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
