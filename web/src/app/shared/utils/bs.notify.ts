declare var $: any;

export class BsNotify {

    static color = {
        INFO: 'info',
        SUCCESS: 'success',
        WARNING: 'warning',
        DANGER: 'danger',
        ROSE: 'rose',
        PRIMARY: 'primary'
    };

    static notify(message: string, icon: string, type: string = '') {
        $.notify({ icon: icon, message: message }, {type: type, timer: 1500, placement: { from: 'top', align: 'right' }});
    }

    static error(message) {
        this.notify(message, 'error_outline', this.color.DANGER);
    }

    static ok(message) {
        this.notify(message, 'done', this.color.SUCCESS);
    }

    static warn(message) {
        this.notify(message, 'warning', this.color.WARNING);
    }

    static info(message) {
        this.notify(message, 'info_outline', this.color.INFO);
    }
}