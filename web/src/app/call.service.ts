import { Http, Headers, RequestOptions, URLSearchParams, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';


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

    getUrl(url: string): string {
        return `${this.protocol}://${this.host}:${this.port}/${url}`;
    }

    get(url: string, params?: any): Observable<Response> {
        let op: URLSearchParams = new URLSearchParams();
        for (let key in params) {
            if (!!params[key]) {
                op.set(key.toString(), params[key]);
            }
        }
        return this._http.get(this.getUrl(url), { search: op })
            .map((res: Response) => res)
            .catch((err: any) => Observable.throw(err));
    }

    post(url: string, body?: any): Observable<Response> {
        return this._http.post(this.getUrl(url), body, json)
            .map((res: Response) => res)
            .catch((err: any) => Observable.throw(err));
    }
}
