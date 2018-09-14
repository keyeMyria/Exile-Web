import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { CallService } from './call.service';
import { Observable, of } from 'rxjs';
import { map, catchError, switchMap } from 'rxjs/operators'

declare var $: any;

export interface CrudConf {
    redirect?: string;
    list?: string;
    add?: string;
    edit?: string;
    delete?: string;
}

export class CrudBase implements Resolve<any> {

    public data: any[];

    protected conf: CrudConf;
    constructor(protected _cl: CallService) {
        this.conf = {};
    }

    protected init(conf: CrudConf) {
        this.conf = conf;
    }

    set addUrl(val: string) {
        this.conf.add = val;
    }

    set editUrl(val: string) {
        this.conf.edit = val;
    }

    set redirectUrl(val: string) {
        this.conf.redirect = val;
    }

    set deleteUrl(val: string) {
        this.conf.delete = val;
    }

    set listUrl(val: string) {
        this.conf.list = val;
    }

    get addUrl() {
        return this.conf.add;
    }
    get editUrl() {
        return this.conf.edit;
    }
    get redirectUrl() {
        return this.conf.redirect;
    }
    get deleteUrl() {
        return this.conf.delete;
    }
    get listUrl() {
        return this.conf.list;
    }

    getById(id) {
        if (id === 0) {
            return of({});
        };
        if (this.data) {
            const res = this.data.filter(item => item.id === id);
            if (!!res[0]) {
                return of(res[0]);
            }
        }
        return this.list({ id: id })
            .pipe(
                map(data => data.object_list[0])
            )
    }

    list(query): Observable<any> {
        if (!!this.conf.list) {
            return this._cl.get(this.conf.list, query, this._cl.json);
        } else {
            throw new SyntaxError('No se ha configurado url para listar');
        }
    }

    add(body: any): Observable<any> {
        if (!!this.conf.add) {
            return this._cl.post(this.conf.add, body);
        } else {
            throw new SyntaxError('No se ha configurado url para agregar');
        }
    }

    edit(id: number, body: any): Observable<any> {
        if (!!this.conf.edit) {
            return this._cl.post(this.conf.edit.replace('$(id)', `${id}`), body);
        } else {
            throw new SyntaxError('No se ha configurado url para editar');
        }
    }

    delete(id: number): Observable<any> {
        if (!!this.conf.delete) {
            return this._cl.delete(this.conf.delete.replace('$(id)', `${id}`));
        } else {
            throw new SyntaxError('No se ha configurado url para borrar');
        }
    }

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): any {
        const id = route.params['id'];
        if (isNaN(+id)) {
            console.log(`Item id was not a number: ${id}`);
            window.location.href = '/#/' + ( !!this.conf.redirect ? this.conf.redirect : '');
            return null;
        }
        return this.getById(+id)
            .pipe(
                map(item => {
                    if (item) {
                        return item;
                    }
                    console.log(`Item was not found: ${id}`);
                    window.location.href = '/#/' + ( !!this.conf.redirect ? this.conf.redirect : '');
                    return of(null);
                }),
                catchError(error => {
                    console.log(`Retrieval error: ${error}`);
                    window.location.href = '/#/' + ( !!this.conf.redirect ? this.conf.redirect : '');
                    return of(null);
                })
            )
    }

    down(aurl: string, id: string, formt: number): void {
        const url = `${this._cl.getUrl(aurl)}${id}`;
        const form = document.createElement('form');
        const input = document.createElement('input');
        const button = document.createElement('button');
        button.setAttribute('type', 'submit');
        input.setAttribute('type', 'hidden');
        input.setAttribute('name', 'file_format');
        input.setAttribute('value', '' + formt);
        form.setAttribute('action', url);
        form.setAttribute('method', 'POST');
        form.setAttribute('target', '_blank');
        form.appendChild(input);
        form.appendChild(button);
        document.body.appendChild(form);
        button.click();
        document.body.removeChild(form);
    }
}



export class CrudService extends CrudBase {

    constructor(protected _cl: CallService, public base_url: string) {
        super(_cl);
        this.setBaseUrl(base_url);
    }
    setBaseUrl(val) {
        this.base_url = val;
        super.init({
            redirect: this.base_url,
            list: `${this.base_url}list/`,
            add: `${this.base_url}form/`,
            edit: `${this.base_url}form/$(id)/`,
            delete: `${this.base_url}delete/$(id)/`
        });
    }
}
