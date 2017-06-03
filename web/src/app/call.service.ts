import { Http, Headers, RequestOptions, URLSearchParams, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

declare var WebSocket: any;

const json = new RequestOptions({
    headers: new Headers({
        'Content-Type': 'application/json'
    })
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
        const op: URLSearchParams = new URLSearchParams();
        for (const key in params) {
            if (!!params[key]) {
                op.set(key.toString(), params[key]);
            }
        }

        return this._http.get(this.getUrl(url), { search: op }).toPromise();
        //     .map((res: Response) => res)
        //     .catch((err: any) => Observable.throw(err));

    }

    post(url: string, body?: any): Promise<Response> {
        console.log(url);
        return this._http.post(this.getUrl(url), body, json).toPromise();
        // .map((res: Response) => res)
        // .catch((err: any) => Observable.throw(err));
    }

    ws(url: string): WebSocket {
        return new WebSocket(this.getUrl(url, 'ws'));
    }
}
