import { Component, OnInit } from '@angular/core';
import { NgForm } from  '@angular/forms';
import { Router } from '@angular/router';

import { LoginService } from './login.service'

declare var $: any;

@Component({
    selector: 'ex-login',
    templateUrl: './login.component.html'
})
export class LoginComponent implements OnInit {

    errorMessage: string;

    constructor(private _ls: LoginService, private _router: Router) { }

    login(loginForm: NgForm) {
        if (loginForm && loginForm.valid) {
            let userName = loginForm.form.value.userName;
            let password = loginForm.form.value.password;
            this._ls.login(userName, password);

            if (this._ls.redirectUrl) {
                this._router.navigateByUrl(this._ls.redirectUrl);
            } else {
                this._router.navigate(['/registro']);
            }
        } else {
            this.errorMessage = 'Please enter a user name and password.';
        };
    }

    ngOnInit() { }

}
