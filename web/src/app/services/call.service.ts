import { Http, Headers, RequestOptions, URLSearchParams, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

declare var WebSocket: any;

const headers = new Headers();
headers.append('Content-Type', 'application/json');

const options = new RequestOptions({
    headers: headers,
    withCredentials: true
});


@Injectable()
export class CallService {

    public protocol: string;
    public host: string;
    public port: string;

    constructor(private _http: Http) {
        this.protocol = 'http';
    }

    conf(chost: string, cport: string, cprotocol?: string) {
        if (cprotocol) {
            this.protocol = cprotocol;
        }
        this.host = chost;
        this.port = cport;
    }

    getUrl(url: string, cprotocol?: string): string {
        const proto = cprotocol || this.protocol;
        return `${proto}://${this.host}:${this.port}/${url}`;
    }

    get(url: string, params?: any): Promise<Response> {
        console.log('get:', url);
        const op: URLSearchParams = new URLSearchParams();
        for (const key in params) {
            if (!!params[key]) {
                op.set(key.toString(), params[key]);
            }
        }
        return this._http.get(this.getUrl(url), options).toPromise();

    }

    post(url: string, body?: any): Promise<Response> {
        console.log('post:', url);
        return this._http.post(this.getUrl(url), body, options).toPromise();
    }

    delete(url: string) {
        console.log('delete:', url);
        return this._http.delete(this.getUrl(url), options).toPromise();
    }

    ws(url: string): WebSocket {
        return new WebSocket(this.getUrl(url, 'ws'));
    }
}
