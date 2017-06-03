import { Component, OnInit } from '@angular/core';

import { AuthService } from '../../auth/auth.service';

@Component({
    selector: 'ex-base',
    templateUrl: './base.component.html'
})

export class BaseComponent implements OnInit {

    constructor(private _as: AuthService) { }

    ngOnInit() {
    }

    logout() {
        this._as.logout();
    }

    isLogin() {
        this._as.isLogin();
    }
}
