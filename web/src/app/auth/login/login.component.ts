import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { AuthService } from '../../shared';

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
        this.form.patchValue({
            username: 'asistente1',
            password: 'admin123456'
        });
    }

    isValid(): boolean {
        return this.form.valid;
    }

    login() {
        console.log('login');
        this.ready = true;
        this._ls.login(this.form.value)
            .then(data => {
                this.ready = false
            })
            .catch(err => {
                this.ready = false;
                if (!!err) {
                    // swal({
                    //     title: err.title,
                    //     text: err.text,
                    //     type: 'warning',
                    //     confirmButtonColor: '#213b78',
                    // });
                    console.log('error', err);
                }
            });
    }

    isLogin() {
        this._ls.isLogin();
    }


    ngOnInit() { }

}
