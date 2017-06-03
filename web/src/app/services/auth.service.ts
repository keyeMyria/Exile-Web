
import { CallService } from './call.service';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../auth/user';

declare var document: any;

@Injectable()
export class AuthService {

    user: User;
    error: any;
    redirectUrl: string;
    sokect: WebSocket;

    constructor(private _cl: CallService, private _rt: Router) { }

    isLoggedIn(): boolean {
        // return true;
        return !!this.getUser();
    }

    addUser(user: User) {
        this.user = user;
        // localStorage.setItem('user', JSON.stringify(this.user));
    }

    getUser(): User {
        if (this.user) {
            return this.user;
        } else {
            const u = JSON.parse(localStorage.getItem('user'));
            if (u) {
                this.addUser(u);
                return u;
            }
        }
        return null;
    }

    login(body: any) {
        if (!body.username && !body.password) {
            return;
        }
        this._rt.navigate([this.redirectUrl || '/dashboard']);
        this._cl.post('usuarios/login/', body)
            .then(data => {
                this.sokect = this._cl.ws('users');
                this.sokect.onmessage = (evn) => {
                    console.log(JSON.parse(evn.data));
                };
                this.addUser(data.json());
                this._rt.navigate([this.redirectUrl || '/dashboard']);
            })
            .catch(err => console.log('error', err));
    }



    logout() {
        this._cl.delete('usuarios/login/')
            .then(res => {
                this.user = null;
                this.redirectUrl = null;
                // this.sokect.close();
                localStorage.removeItem('user');
                this._rt.navigate(['/login']);
            })
            .catch(err => console.log('error', err));
    }

    isLogin() {
        this._cl.get('usuarios/is/login/')
            .then(res => console.log('then:', res))
            .catch(err => console.log('catch', err));
    }
}
