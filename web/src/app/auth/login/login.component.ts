import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { AuthService } from '../auth.service';

declare var $: any;
declare var swal: any;

@Component({
    selector: 'ex-login',
    templateUrl: './login.component.html'
})

export class LoginComponent implements OnInit {

    form: FormGroup;
    ready = false;

    constructor(private _ar: ActivatedRoute, private _ls: AuthService, private _fb: FormBuilder) {

        this.form = this._fb.group({
            username: ['', Validators.required],
            password: ['', Validators.required]
        });
    }

    isValid(): boolean {
        return this.form.valid;
    }

    login() {
        this.ready = true;
        this._ls.login(this.form.value)
            .then(data => this.ready = false)
            .catch(err => {
                this.ready = false;
                if (!!err) {
                    swal({
                        title: 'Inicio de sesión fallido',
                        text: 'El correo electrónico o la contraseña no son válidos.',
                        type: 'warning',
                        confirmButtonColor: '#213b78',
                    });
                }
            });
    }

    isLogin() {
        this._ls.isLogin();
    }


    ngOnInit() { }

}
