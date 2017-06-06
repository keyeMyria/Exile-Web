
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
        return !!this.getUser();
    }

    private addUser(user: User) {
        this.user = user;
        localStorage.setItem('user', JSON.stringify(this.user));
        if(!this.sokect) {
            this.sokect = this._cl.ws('users');
        }
    }

    private removeUser(err?) {
        console.log(err);
        this.user = null;
        this.redirectUrl = null;
        if (!!this.sokect) {
            this.sokect.close();
        }
        localStorage.removeItem('user');
        this._rt.navigate(['/login']);
    }

    getUser(): User {
        if (this.user) {
            return this.user;
        } else {
            this.isLogin();
            const u = JSON.parse(localStorage.getItem('user'));
            if (u) {
                this.addUser(u);
                return u;
            }
            return null;
        }
    }

    login(body: any) {
        if (!body.username && !body.password) {
            return;
        }
        this._cl.post('usuarios/login/', body)
            .then(res => res.json())
            .then(data => {
                this.addUser(data);
                this._rt.navigate([this.redirectUrl || '/dashboard']);
            })
            .catch(err => console.log('error', err));
    }

    logout() {
        this._cl.delete('usuarios/login/')
            .then(res => res.json())
            .then(data => {
                this.removeUser();
            })
            .catch(err => console.log('error', err));
    }

    isLogin() {
        return this._cl.get('usuarios/is/login/')
            .then(res => res.json())
            .then(data => console.log(data))
            .catch(err => this.removeUser(err));
    }
}
