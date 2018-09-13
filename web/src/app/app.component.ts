import { Component, OnInit } from '@angular/core';
import { CallService, AuthService } from './shared';
import { Menu } from './shared';
import { UsuariosMenuMeta } from './usuarios/route';
import { OperacionMenuMeta } from './operacion/route';
import { ConfiguracionMenuMeta } from './configuracion/route';
import { NovedadesMenuMeta } from './novedades/route';

declare var $: any;

@Component({
    selector: 'ex-nomina',
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
    constructor(private _cs: CallService, private _as: AuthService) {
        this._cs.conf({ host: 'ec2-18-223-116-221.us-east-2.compute.amazonaws.com', port: '8081' });
        this._as.conf('usuarios/login/', 'usuarios/is/login/');
        // this._cs.conf({ host: 'isabela.com.co' });
    }
    ngOnInit() {
        $.material.init();
        Menu.instance.addMenu({ title: 'Inico', url: '/dashboard', icon: 'dashboard' });
        Menu.instance.addMenu({ title: 'Usuarios', icon: 'supervisor_account', children: UsuariosMenuMeta })
        Menu.instance.addMenu({ title: 'Operación', icon: 'build', children: OperacionMenuMeta })
        Menu.instance.addMenu({ title: 'Novedades', icon: 'priority_high', children: NovedadesMenuMeta })
        Menu.instance.addMenu({ title: 'Configuración', icon: 'settings', children: ConfiguracionMenuMeta })

    }
}
