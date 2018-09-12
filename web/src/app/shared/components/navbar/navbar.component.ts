import { Component, Input } from '@angular/core';
// import { AuthService } from '../../app/auth/auth.service';
@Component({
    selector: 'ex-navbar',
    templateUrl: 'navbar.component.html',
})
export class NavbarComponent {

    @Input('right') public right = false;
    @Input('mobile') public mobile = false;

    constructor(/*public _as: AuthService*/) { }
}
