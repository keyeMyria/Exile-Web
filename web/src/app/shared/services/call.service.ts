import { HttpClient, HttpHeaders, HttpResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { catchError, map, switchMap} from 'rxjs/operators';

declare var ReconnectingWebSocket: any;
declare var window: any;
declare var channels: any;

export interface Ip {
    protocol?: string;
    port?: string;
    host: string;
}

export interface ExError {
    error: any;
    title?: string;
    text?: string;
}



@Injectable()
export class CallService {

    public json: any = { 'Content-Type': 'application/json' };
    public _ip: Ip;


    constructor(private _http: HttpClient) {
        window._server = this.ip;
    }

    /**
     * asigna una configuracion segun la cual se aran solicitudes Http
     * @param  {Ip} ip  ip a la cual estaran dirigidas las solicitud Http
     */
    public conf(ip: Ip): void {
        this._ip = ip;
        window._server = this.ip;
    }

    /**
     * ip a la cual estaran dirigidas las solicitud Http
     * @return {string} ip
     */
    public get ip(): string {
        if (!!this._ip) {
            return this.construcIP(this._ip.protocol, this._ip.host, this._ip.port);
        }
        return '';
    }

    /**
     * construye una cadena ip apartir de los parametros recividos
     * @param  {string = 'http'}      proto protocolo
     * @param  {string = '0.0.0.0'}   host  destino
     * @param  {string = ''}          port  puerto
     * @return {string}      cadena ip
     */
    private construcIP(proto: string = 'http', host: string = '0.0.0.0', port: string = ''): string {
        return `${proto}://${this._ip.host}:${port}`
    }

    /**
     * construye las urls sobre las cuales se realizaran solicitudes
     * @param  {string} url   url base
     * @param  {string} proto protocolo
     * @return {string}       cadena ip
     */
    public getUrl(url: string, proto?: string): string {
        let ip;
        let auxUrl = `/${url}`;
        if (!!this._ip && !!proto) {
            ip = this.construcIP(proto, this._ip.host, this._ip.port);
        } else {
            ip = this.ip;
        }
        if (ip) {
            auxUrl = `${ip}${auxUrl}`;
        }
        return auxUrl;
    }

    /**
     * construye las RequestOptions a ser enviadas en las consultas Http
     * @param  {any}            headersList lista de cabeseras a enviar
     * @param  {any}            par         lista de parametros a enviar (json)
     * @return {RequestOptions}
     */
    private getOptions(headersList: any, par?: any): Object {
        return {
            headers: {
                ...headersList
            },
            params: {
                ...par 
            },
            withCredentials: true
        };
    }

    /**
     * [get description]
     * @param  {string}          url    [description]
     * @param  {any}             params [description]
     * @param  {any}             head   [description]
     * @return {Observable<any>}        [description]
     */
    get(url: string, params?: any, head?: any): Observable<any> {
        return this._http
            .get(this.getUrl(url), this.getOptions(head, params))
            .pipe(
                catchError(this.error)
            );
    }

    /**
     * [delete description]
     * @param  {string}          url  [description]
     * @param  {any}             head [description]
     * @return {Observable<any>}      [description]
     */
    delete(url: string, head?: any): Observable<any> {
        return this._http
            .delete(this.getUrl(url), this.getOptions(head))
            .pipe(
                catchError(this.error)
            );

    }

    /**
     * [head description]
     * @param  {string}          url  [description]
     * @param  {any}             head [description]
     * @return {Observable<any>}      [description]
     */
    head(url: string, head?: any): Observable<any> {
        return this._http
            .delete(this.getUrl(url), this.getOptions(head))
            .pipe(
                catchError(this.error)
            );
    }

    /**
     * [post description]
     * @param  {string}          url  [description]
     * @param  {any}             body [description]
     * @param  {any}             head [description]
     * @return {Observable<any>}      [description]
     */
    post(url: string, body?: any, head?: any): Observable<any> {
        return this._http
            .post(this.getUrl(url), body, this.getOptions(head))
            .pipe(
                catchError(this.error)
            );
    }

    /**
     * [put description]
     * @param  {string}          url  [description]
     * @param  {any}             body [description]
     * @param  {any}             head [description]
     * @return {Observable<any>}      [description]
     */
    put(url: string, body?: any, head?: any): Observable<any> {
        return this._http
            .put(this.getUrl(url), body, this.getOptions(head))
            .pipe(
                catchError(this.error)
            );
    }

    /**
     * [patch description]
     * @param  {string}          url  [description]
     * @param  {any}             body [description]
     * @param  {any}             head [description]
     * @return {Observable<any>}      [description]
     */
    patch(url: string, body?: any, head?: any): Observable<any> {
        return this._http
            .patch(this.getUrl(url), body, this.getOptions(head))
            .pipe(
                catchError(this.error)
            );
        
    }

    /**
     * [error description]
     * @param  {[type]}              error [description]
     * @return {Observable<ExError>}       [description]
     */
    private error(error): Observable<ExError> {
        let res: ExError;
        switch (error.status) {
            case 0:
                res = {
                    title: 'Sin Conexión!',
                    text: 'Verifique su Conexión a Internet.',
                    error: error
                };
                break;
            case 400:
                res = {
                    title: '400',
                    text: '400',
                    error: error
                };
                break;
            case 403:
                res = {
                    title: 'Sin Acceso!',
                    text: 'Usted no tiene permitido realizar este cambio.',
                    error: error
                };
                break;
            case 404:
                res = {
                    title: 'No se pudo encontrar el objeto!',
                    error: error
                };
                break;
            case 408:
                res = {
                    title: 'Su solicitud ha tardado mucho tiempo!',
                    text: 'Por favor verifique su Conexión a Internet y vuelva a intentarlo.',
                    error: error
                };
                break;
            default:
                res = { error: error };
                break;
        }
        return Observable.throw(res);
    }

}



@Injectable()
export class WebsocketService {

    private subjects = [];
    public _mgs: Subject<any>;
    private ws: any;

    constructor() {
        if (!this._mgs) {
            this._mgs = new Subject();
        }
        if (!this.ws) {
            this.ws = new channels.WebSocketBridge();
        }
    }

    public mgs(type?: string) {
        if (!type) {
            return this._mgs;
        } else {
            const aux = this.subjects.filter(item => item.type === type)[0];
            const subject = !aux ? this.demultiplex(type) : aux.subject;
            this.subjects.push({ type, subject });
            return subject;
        }
    }

    public connect(url: string) {
        this.ws.connect(url);
        this.ws.listen(data => this._mgs.next(data));
        this.ws.socket.addEventListener('open', function() {
            console.log("Connected to WebSocket");
        });
        this.ws.socket.addEventListener('close', function() {
            console.log("Disconnected to WebSocket");
        });
    }

    private demultiplex(type: string): Subject<any> {
        const subject = new Subject();
        this.ws.demultiplex(type, action => subject.next(action));
        return subject;
    }

    public send(data) {
        this.ws.send(data)
    }

}
