import { CallService } from '../../../call.service';
import { Injectable } from '@angular/core';
import { User } from './user';

@Injectable()
export class AuthService {

    user: User;
    error: any;
    redirectUrl: string;

    constructor(private _cl: CallService) { }

    isLoggedIn(): boolean {
        return !!this.getUser();
    }

    addUser(user: User) {
        this.user = user;
        localStorage.setItem('user', JSON.stringify(this.user));
    }

    getUser(): User {
        if (this.user) {
            return this.user;
        } else {
            let u = JSON.parse(localStorage.getItem('user'));
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
        return this._cl.post('usuarios/login/', body);
    }

    logout() {
        return this._cl.get('usuarios/logout/').subscribe(res => {
            localStorage.clear();
            return res.ok;
        }, err => err.ok);
    }
}
