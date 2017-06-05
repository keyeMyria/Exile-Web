import { Http, Headers, RequestOptions, URLSearchParams, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

declare var WebSocket: any;







@Injectable()
export class CallService {

    public protocol: string;
    public host: string;
    public port: string;


    constructor(private _http: Http) {
        this.protocol = 'http';
    }

    getOptions(headersList: any, par?: URLSearchParams): RequestOptions {
        const headers = new Headers();
        for (const key in headersList) {
            if (headersList[key]) {
                headers.append(key, headersList[key]);
            }
        }
        return new RequestOptions({
            headers: headers,
            // withCredentials: true,
            search: par ? par : new URLSearchParams()
        });
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

    get(url: string, params?: any, head?: any): Promise<Response> {
        console.log('get:', url);
        const query = new URLSearchParams();
        for (const key in params) {
            if (params[key]) {
                query.set(key, params[key]);
            }
        }
        return this._http.get(this.getUrl(url), this.getOptions(head)).toPromise();

    }


    delete(url: string, head?: any) {
        console.log('delete:', url);
        return this._http.delete(this.getUrl(url), this.getOptions(head)).toPromise();
    }

    head(url: string, head?: any) {
        console.log('delete:', url);
        return this._http.delete(this.getUrl(url), this.getOptions(head)).toPromise();
    }

    post(url: string, body?: any, head?: any): Promise<Response> {
        console.log('post:', url);
        return this._http.post(this.getUrl(url), body, this.getOptions(head)).toPromise();
    }


    put(url: string, body?: any, head?: any): Promise<Response> {
        console.log('put:', url);
        return this._http.put(this.getUrl(url), body, this.getOptions(head)).toPromise();
    }

    patch(url: string, body?: any, head?: any): Promise<Response> {
        console.log('patch:', url);
        return this._http.patch(this.getUrl(url), body, this.getOptions(head)).toPromise();
    }

    ws(url: string): WebSocket {
        return new WebSocket(this.getUrl(url, 'ws'));
    }
}
