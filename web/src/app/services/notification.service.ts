import { Injectable } from '@angular/core';

declare var $: any;

@Injectable()
export class NotificationService {

    public color = {
        info: 'info',
        success: 'success',
        warning: 'warning',
        danger: 'danger',
        rose: 'rose',
        primary: 'primary'
    };

    constructor() { }

    notify(message: string, icon: string, type: string = '') {
        $.notify(
            { icon: icon, message: message },
            {
                type: type,
                timer: 1500,
                placement: {
                    from: 'top',
                    align: 'right'
                }
            }
        );
    }

    error(message) {
        this.notify(message, 'error_outline', this.color.danger);
    }

    ok(message) {
        this.notify(message, 'done', this.color.success);
    }

    warn(message) {
        this.notify(message, 'warning', this.color.warning);
    }

    info(message) {
        this.notify(message, 'info_outline', this.color.info);
    }
}
