import { Injectable } from '@angular/core';

import { User} from './user';

@Injectable()
export class LoginService {
    user: User;
    redirectUrl: string;

    constructor() { }

    isLoggedIn() {
        return !!this.user;
    }

    login(username: string, pass: string) {
        if (!username || !pass) {
            return;
        }
        this.user = {
            id: 2,
            username: username,
            isAdmin: false
        };
    }

    logout() {
        this.user = null;
    }
}
