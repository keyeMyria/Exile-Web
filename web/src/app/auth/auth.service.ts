import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CallService } from '../../lib/services/call.service';
import { User } from './user';

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
        localStorage.setItem('user', JSON.stringify(user));
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
            this.isLogin().then(data => {
                this.addUser(data);
            });
            if (localStorage.hasOwnProperty('user') && localStorage.user !== 'undefined') {
                const u = JSON.parse(localStorage.getItem('user'));
                this.addUser(u);
                return u;
            }
            return null;
        }
    }

    login(body: any) {
        if (!body.username && !body.password) {
            return Promise.reject(null);
        }
        return this._cl.post('usuarios/login/', body)
            .then(res => res.json())
            .then(data => {
                this.addUser(data);
                this._rt.navigate([this.redirectUrl || '/']);
                return Promise.resolve(data);
            })
            .catch(err => {
                return Promise.reject(err);
            });
    }

    logout() {
        this._cl.delete('usuarios/login/')
            .then(data => {
                this.removeUser();
            })
            .catch(err => console.log('error', err));
    }

    isLogin() {
        return this._cl.get('usuarios/is/login/')
            .then(res => res.json())
            // .then(data => console.log(data))
            .catch(err => this.removeUser(err));
    }
}
