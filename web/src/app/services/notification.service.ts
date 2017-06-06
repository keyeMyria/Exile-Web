import { Injectable } from '@angular/core';

declare var $: any;

@Injectable()
export class NotificationService {

    constructor() { }
    notyfy(message: string, icon: string, type: string = '') {
        $.notify(
            { icon: icon, message: message},
            { type: type, placement: {
                from: 'top',
                align: 'right'
            }
        });
    }
}
