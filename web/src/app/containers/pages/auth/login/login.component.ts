import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { AuthService } from '../auth.service';

declare var $: any;

@Component({
    selector: 'ex-login',
    templateUrl: './login.component.html'
})

export class LoginComponent implements OnInit {

    form: FormGroup;
    returnUrl: string;

    constructor(
        private _ls: AuthService,
        private _fb: FormBuilder,
        private _ar: ActivatedRoute,
        private _rt: Router) {

        this.form = this._fb.group({
            username: ['', Validators.required],
            password: ['', Validators.required]
        });
        this.form.patchValue({
            username: 'admin',
            password: 'admin123456'
        });
    }

    isValid(): boolean {
        return this.form.valid;
    }

    login() {
        this._ls.login(this.form.value).subscribe(data => {
            this._ls.addUser(data.json());
            this._rt.navigate([this.returnUrl]);
        }, err => {
            console.log(err);
        });
    }

    logout() {
        if (this._ls.logout()) {
            console.log('Out ok');
        }
    }

    ngOnInit() {
        this.returnUrl = this._ar.snapshot.queryParams['returnUrl'] || '/dashboard/';
        if (this._ls.getUser()) {
            console.log(this.returnUrl);
            this._rt.navigate([this.returnUrl]);
        }
    }

}
