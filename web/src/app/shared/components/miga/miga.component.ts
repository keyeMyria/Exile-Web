import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';

interface Miga {
    name: string;
    url: string;
}

@Component({
    selector: 'ex-miga',
    templateUrl: 'miga.component.html',
})
export class MigaComponent implements OnInit {

    public migas: Miga[];

    constructor(private _rt: Router, private _art: ActivatedRoute) {
        this.migas = [];
    }

    ngOnInit() {
        this.migas = this.getMigas(this._art);
        this._rt.events
            .pipe(
                filter(event => event instanceof NavigationEnd)
            )
            .subscribe(event => {
                this.migas = this.getMigas(this._art);
            });
    }

    getMigas(route: ActivatedRoute, url: string = '', migas: Miga[] = []): Miga[] {
        const routeURL = route.snapshot.url.map(segment => segment.path).join('/');
        if (routeURL !== '') {
            url += `/${routeURL}`;
            if (route.snapshot.data.hasOwnProperty('miga')) {
                let title = route.snapshot.data['miga'];
                if (route.snapshot.params.hasOwnProperty('id') && title === 'Editar') {
                    title = route.snapshot.params['id'] === '0' ? 'Agregar' : title;
                }
                const miga: Miga = {
                    name: title,
                    url: url,
                };
                migas.push(miga);
            }
        }
        if (!!route.firstChild) {
            this.getMigas(route.firstChild, url, migas)
        }
        return migas;
    }
}
