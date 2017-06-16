import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { AuthService } from '../../services/auth/auth.service';

declare var $: any;

@Component({
    selector: 'ex-login',
    templateUrl: './login.component.html'
})

export class LoginComponent implements OnInit {

    form: FormGroup;

    constructor(private _ar: ActivatedRoute, private _ls: AuthService, private _fb: FormBuilder) {

        this.form = this._fb.group({
            username: ['', Validators.required],
            password: ['', Validators.required]
        });
        this.form.patchValue({
            username: 'asistente1',
            password: 'admin123456'
        });
    }

    isValid(): boolean {
        return this.form.valid;
    }

    login() {
        this._ls.login(this.form.value);
    }

    isLogin() {
        this._ls.isLogin();
    }


    ngOnInit() { }

}
