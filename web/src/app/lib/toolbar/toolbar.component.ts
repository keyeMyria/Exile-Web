import { Component, OnInit, Renderer, ViewChild, ElementRef, Directive  } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Location, LocationStrategy, PathLocationStrategy } from '@angular/common';
import { AuthService } from '../../services/auth/auth.service';
import { NotificationService } from '../../services/notification.service';
import { AppMenuMeta } from '../../app.routing';

declare var $: any;

@Component({
    selector: 'ex-toolbar',
    templateUrl: './toolbar.component.html'
})
export class ToolbarComponent implements OnInit {

    private listTitles: any[];
    location: Location;
    private nativeElement: Node;
    private toggleButton;
    private sidebarVisible: boolean;

    @ViewChild('navbar-cmp') button;

    constructor(
        location: Location,
        private renderer: Renderer,
        private element: ElementRef,
        private _as: AuthService,
        private _ns: NotificationService) {

        this.location = location;
        this.nativeElement = element.nativeElement;
        this.sidebarVisible = false;
    }

    ngOnInit() {
        // this._as.sokect.onmessage = (evn) => {
        //     const data = JSON.parse(evn.data);
        //     this._ns.notyfy(`El usuario <b>${data.username}</b> se ha conectado`, 'notifications', 'info');
        // };
        const navbar: HTMLElement = this.element.nativeElement;
        this.toggleButton = navbar.getElementsByClassName('navbar-toggle')[0];
        this.listTitles =  AppMenuMeta.filter(menuItem => menuItem);
    }
    isMobileMenu() {
        if ($(window).width() < 991) {
            return false;
        }
        return true;
    }
    sidebarToggle() {
        const toggleButton = this.toggleButton;
        const body = document.getElementsByTagName('body')[0];

        if (this.sidebarVisible === false) {
            setTimeout(function() {
                toggleButton.classList.add('toggled');
            }, 500);
            body.classList.add('nav-open');
            this.sidebarVisible = true;
        } else {
            this.toggleButton.classList.remove('toggled');
            this.sidebarVisible = false;
            body.classList.remove('nav-open');
        }
    }

    getTitle() {
        // let titlee = this.location.prepareExternalUrl(this.location.path());
        // if (titlee.charAt(0) === '#') {
        //     titlee = titlee.slice(2);
        // }
        // for (let item = 0; item < this.listTitles.length; item++) {
        //     if (this.listTitles[item].path === titlee) {
        //         return this.listTitles[item].title;
        //     }
        // }
        return 'Exile';
    }
    getPath() {
        // console.log(this.location);
        return this.location.prepareExternalUrl(this.location.path());
    }

    logout() {
        this._as.logout();
    }

    isLogin() {
        this._as.isLogin();
    }

}
