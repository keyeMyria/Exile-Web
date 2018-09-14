import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Http } from '@angular/http';
import { CallService, WebsocketService } from './call.service';
import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/filter';
declare var document: any;

// export interface User {
//     id: number;
//     username: string;
//     first_name: string;
//     last_name: string;
//     email: string;
//     date_joined: Date;
//     last_login: Date;
//     is_active: boolean;
//     is_staff: boolean;
//     is_superuser: boolean;
// }

@Injectable()
export class AuthService {

    user: any;
    error: any;
    redirectUrl: string;
    sokect: WebSocket;
    serviceUrl: string;
    isLogUrl: string;

    constructor(private _cl: CallService, private _ws: WebsocketService, private _rt: Router) { }

    public conf(url: string, log: string){
        this.serviceUrl = url;
        this.isLogUrl = log;
    }

    isLoggedIn(): boolean {
        return !!this.getUser();
    }


    private addUser(user: any) {
        console.log(user);
        this.user = user;
        localStorage.setItem('user', JSON.stringify(user));
        const ws = user.ws ? user.ws : user.username;
        const ip = this._cl.getUrl(ws, 'ws');
        this._ws.connect(ip)
        this._ws.mgs().subscribe(noc => console.log(noc));
        this._ws.mgs('asistente').filter(item => item.pk === 11).subscribe(noc => console.log(noc));


    }
    private removeUser(err?) {
        this.user = null;
        this.redirectUrl = null;
        localStorage.removeItem('user');
        this._rt.navigate(['/login']);
    }

    getUser(): any {
        this.isLogin().catch(err => this.removeUser(err));
        if (this.user) {
            return this.user;
        } else {
            if (localStorage.hasOwnProperty('user') && localStorage.user !== 'undefined') {
                const u = JSON.parse(localStorage.getItem('user'));
                this.addUser(u);
                return u;
            }
        }
        return null;
    }

    login(body: any) {
        if (!body.username && !body.password && this.serviceUrl) {
            return Promise.reject(null);
        }
        return this._cl.post(this.serviceUrl, body)
            .toPromise()
            .then(res => res)
            .then(() => {
                return this.isLogin()
                    .then(data => {
                        console.log(data);
                        this._rt.navigate([this.redirectUrl || '/']);
                        this.addUser(data);
                        return Promise.resolve(data);
                    })
                    .catch(err => Promise.reject(err));
            })
            .catch(err => Promise.reject(err));
    }

    logout() {
        if (!!this.serviceUrl) {
            this._cl.delete(this.serviceUrl)
                .toPromise()
                .then(data => {
                    this.removeUser();
                })
                .catch(err => console.log('error', err));
        }
        
    }

    isLogin() {
        return this._cl.get(this.isLogUrl)
            .toPromise()
            .then(res => res)
            .catch(err => this.removeUser(err));
    }
}
