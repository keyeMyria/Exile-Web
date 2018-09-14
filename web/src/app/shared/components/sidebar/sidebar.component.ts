import { Component, OnInit } from '@angular/core';
import { Menu } from '../../services/menu';

declare var $: any;
declare var window: any;

@Component({
    selector: 'ex-sidebar',
    templateUrl: './sidebar.component.html'
})
export class SidebarComponent implements OnInit {

    menuInfo: any[];

    user: any;

    constructor() {
        if (localStorage.hasOwnProperty('user') && localStorage.user !== 'undefined') {
            this.user = JSON.parse(localStorage.getItem('user'));
            if (!!this.user.avatar) {
                this.user.avatar = `url(${window._server}${this.user.avatar})`;
            } else {
                this.user['avatar'] = 'url(/assets/img/default-avatar.png)';
            }
            if (!!this.user.first_name) {
                this.user['nombre'] = this.user.first_name;
            }
            if (!!this.user.last_name) {
                this.user['apellidos'] = this.user.last_name;
            }
        } else {
            this.user['nombre'] = 'Usuario';
            this.user['avatar'] = 'url(/assets/img/default-avatar.png)';
        }
    }

    ngOnInit() {
        $.getScript('../../assets/js/sidebar-moving-tab.js');
        this.menuInfo = Menu.instance.menuList.filter(menuItem => menuItem);
    }

    isNotMobileMenu() {
        if ($(window).width() > 991) {
            return false;
        }
        return true;
    }

}
