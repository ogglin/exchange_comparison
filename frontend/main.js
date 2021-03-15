(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! C:\angularProjects\excomparison\src\main.ts */"zUnb");


/***/ }),

/***/ "0d3g":
/*!***************************************************************!*\
  !*** ./src/app/components/main-table/main-table.component.ts ***!
  \***************************************************************/
/*! exports provided: MainTableComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MainTableComponent", function() { return MainTableComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _angular_material_table__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/material/table */ "+0xr");
/* harmony import */ var _services_api_service_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../services/api-service.service */ "ul72");
/* harmony import */ var _socket_socket_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../socket/socket.component */ "F5WS");
/* harmony import */ var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/material/form-field */ "kmnG");
/* harmony import */ var _angular_material_input__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/material/input */ "qFsG");
/* harmony import */ var _angular_material_sort__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @angular/material/sort */ "Dh3D");
/* harmony import */ var _notice_notice_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../notice/notice.component */ "dlut");
/* harmony import */ var _angular_material_button__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @angular/material/button */ "bTqV");
/* harmony import */ var _angular_material_icon__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @angular/material/icon */ "NFeN");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @angular/common */ "ofXK");













function MainTableComponent_th_10_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 16);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " \u041F\u0430\u0440\u0430 ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function MainTableComponent_td_11_Template(rf, ctx) { if (rf & 1) {
    const _r14 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 17);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "button", 18);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function MainTableComponent_td_11_Template_button_click_2_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r14); const element_r12 = ctx.$implicit; const ctx_r13 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"](); return ctx_r13.hidePair(element_r12.pair, element_r12.buy_name, element_r12.sell_name, element_r12.percent); });
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-icon", 19);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4, "remove_red_eye");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const element_r12 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", element_r12.pair, " ");
} }
function MainTableComponent_th_13_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 16);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " Buy ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function MainTableComponent_td_14_ng_container_2_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const element_r15 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("btc: ", element_r15.buy_ask, "");
} }
function MainTableComponent_td_14_Template(rf, ctx) { if (rf & 1) {
    const _r19 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function MainTableComponent_td_14_Template_td_click_0_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r19); const element_r15 = ctx.$implicit; const ctx_r18 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"](); return ctx_r18.toUrl(element_r15.buyurl); });
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, MainTableComponent_td_14_ng_container_2_Template, 3, 1, "ng-container", 21);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const element_r15 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate2"](" ", element_r15.buy_name.replace("hitbtc", "HITbtc"), " | ", element_r15.buy, " ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", element_r15.pair.includes("BTC"));
} }
function MainTableComponent_th_16_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 16);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " Sell ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function MainTableComponent_td_17_ng_container_2_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const element_r20 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("btc: ", element_r20.sell_bid, "");
} }
function MainTableComponent_td_17_Template(rf, ctx) { if (rf & 1) {
    const _r24 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function MainTableComponent_td_17_Template_td_click_0_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r24); const element_r20 = ctx.$implicit; const ctx_r23 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"](); return ctx_r23.toUrl(element_r20.sellurl); });
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, MainTableComponent_td_17_ng_container_2_Template, 3, 1, "ng-container", 21);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const element_r20 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate3"](" ", element_r20.sell_name.replace("hitbtc", "HITbtc"), " (", element_r20.sell_symbol, ") | ", element_r20.sell, " ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", element_r20.sell_symbol.includes("BTC"));
} }
function MainTableComponent_th_19_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 16);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " \u041F\u0440\u043E\u0446\u0435\u043D\u0442 ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function MainTableComponent_td_20_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 17);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const element_r25 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", element_r25.percent, "% ");
} }
function MainTableComponent_tr_21_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 22);
} }
const _c0 = function (a0) { return { "background-color": a0 }; };
function MainTableComponent_tr_22_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 23);
} if (rf & 2) {
    const row_r26 = ctx.$implicit;
    const ctx_r10 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngStyle", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction1"](1, _c0, row_r26.percent >= ctx_r10.redKoef ? ctx_r10.color.red : ctx_r10.color.green));
} }
function MainTableComponent_tr_23_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "tr", 24);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "td", 25);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("No data matching \"", _r0.value, "\"");
} }
class MainTableComponent {
    constructor(api, ngZone) {
        this.api = api;
        this.ngZone = ngZone;
        this.color = {
            grey: '#bfbfbf',
            green: '#a8dab5',
            red: '#f44336' // 5<
        };
        this.ExchangeData = [];
        this.TableData = [];
        this.tempTableData = [];
        this.displayedColumns = ['pair', 'buy', 'sell', 'percent'];
        this.dataSource = new _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatTableDataSource"](this.TableData);
        this.greenKoef = 2.5;
        this.redKoef = 5;
        this.pushKoef = 1;
        this.timer = 2000;
        this.apiKeys = [];
        this.tokenPrices = [];
        this.notices = [];
        this.noticesTimer = 10;
        this.freezePercent = 1;
        this.settingsModules = {
            bancor: true,
            idex: true,
            kyber: true,
            uniswap_v2: true,
            uniswap_v1: true,
        };
        this.hideDirection = [];
        this.init = () => {
            this.api.getApi('settings').subscribe((result) => {
                this.apiKeys = result[0].api_keys.keys;
                this.timer = result[0].timeout_refresh_data;
                this.noticesTimer = result[0].timeout_notice;
                this.redKoef = result[0].koef_top;
                this.greenKoef = result[0].koef_low;
                this.pushKoef = result[0].koef_push;
                this.freezePercent = result[0].freeze_percent;
                this.gasNormal = result[0].gas_normal;
                this.gasFast = result[0].gas_fast;
            });
            this.api.getApi('settings_modules').subscribe((result) => {
                result.forEach(r => {
                    switch (r.module_name) {
                        case 'bancor':
                            this.settingsModules.bancor = r.is_active;
                            break;
                        case 'idex':
                            this.settingsModules.idex = r.is_active;
                            break;
                        case 'kyber':
                            this.settingsModules.kyber = r.is_active;
                            break;
                        case 'uniswap_v2':
                            this.settingsModules.uniswap_v2 = r.is_active;
                            break;
                        case 'uniswap_v1':
                            this.settingsModules.uniswap_v1 = r.is_active;
                            break;
                    }
                });
            });
            this.getHotbitProfits();
            // this.getPair();
            // this.ngZone.runOutsideAngular(() => {
            // setInterval(() => {
            //   this.getPair();
            // }, this.timer);
            // });
        };
        this.getPair = () => {
            this.api.getApi('exchpair/').subscribe((result) => {
                this.tokenPrices = result;
                setTimeout(() => {
                    this.getPair();
                }, this.timer);
            }, error => {
                console.log(error);
                this.getPair();
            });
        };
        this.getHotbitProfits = () => {
            this.api.getApi('settings').subscribe((result) => {
                this.apiKeys = result[0].api_keys.keys;
                this.timer = result[0].timeout_refresh_data;
                this.noticesTimer = result[0].timeout_notice;
                this.redKoef = result[0].koef_top;
                this.greenKoef = result[0].koef_low;
                this.pushKoef = result[0].koef_push;
                this.freezePercent = result[0].freeze_percent;
                this.gasNormal = result[0].gas_normal;
                this.gasFast = result[0].gas_fast;
            });
            this.api.getApi('exchpair/').subscribe((result) => {
                this.tokenPrices = result;
            });
            this.api.getApi('profit_exchanges/').subscribe(res => {
                this.TableData = [];
                res.forEach(item => {
                    let isHide = false;
                    this.hideDirection.forEach(hide => {
                        if (hide.pair === item.pair && hide.buy === item.buy_name && hide.sell === item.sell_name) {
                            isHide = !Number(((item.sell - item.buy) / (item.buy / 100)).toFixed(2)) <= hide.percent + this.freezePercent;
                        }
                    });
                    if (!isHide) {
                        const elem = {
                            pair: item.pair,
                            buy_name: item.buy_name,
                            buy: item.buy,
                            sell_name: item.sell_name,
                            sell: item.sell,
                            percent: item.percent,
                            tokenid: item.tokenid,
                            buyurl: item.buyurl,
                            sellurl: item.sellurl,
                            buy_ask: item.buy_ask,
                            sell_bid: item.sell_bid,
                            sell_symbol: item.sell_symbol
                        };
                        this.TableData.push(elem);
                    }
                });
                this.TableData.sort((a, b) => {
                    if (a.percent < b.percent) {
                        return 1;
                    }
                    if (a.percent > b.percent) {
                        return -1;
                    }
                    // a должно быть равным b
                    return 0;
                });
                this.dataSource = new _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatTableDataSource"](this.TableData);
                this.pushNotice(this.checkChange(this.TableData));
                setTimeout(() => {
                    this.getHotbitProfits();
                }, this.timer);
            }, error => {
                console.log(error);
                this.getHotbitProfits();
            });
        };
        this.checkChange = (newData) => {
            const changes = [];
            if (this.tempTableData.length < 1) {
                this.tempTableData = newData;
                this.tempTableData.forEach((el) => {
                    if (el.percent > this.redKoef) {
                        changes.push(el);
                    }
                });
            }
            else {
                this.TableData.forEach((el) => {
                    if (el.percent > this.redKoef && this.checkElem(el, this.tempTableData) !== true) {
                        changes.push(el);
                    }
                });
                this.tempTableData = newData;
            }
            return changes;
        };
        this.checkElem = (elem, array) => {
            const isBelowThreshold = (currentValue) => JSON.stringify(currentValue) === JSON.stringify(elem);
            return array.some(isBelowThreshold);
        };
        this.pushNotice = (notice) => {
            this.notices = notice;
        };
        this.applyFilter = (event) => {
            const filterValue = event.target.value;
            this.dataSource.filter = filterValue.trim().toLowerCase();
        };
        this.toUrl = (url) => {
            const a = document.createElement('a');
            a.setAttribute('href', url);
            a.dispatchEvent(new MouseEvent('click', { ctrlKey: true }));
        };
        this.hidePair = (pair, buy, sell, percent) => {
            this.hideDirection.push({ pair, buy, sell, percent });
            console.log(this.hideDirection);
        };
    }
    ngOnInit() {
        this.init();
    }
}
MainTableComponent.ɵfac = function MainTableComponent_Factory(t) { return new (t || MainTableComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_api_service_service__WEBPACK_IMPORTED_MODULE_2__["ApiServiceService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgZone"])); };
MainTableComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: MainTableComponent, selectors: [["app-main-table"]], decls: 25, vars: 11, consts: [[3, "API_KEYS", "tokenPrices"], ["matInput", "", "placeholder", "\u041D\u0430\u0439\u0442\u0438", 3, "keyup"], ["input", ""], [2, "text-align", "right", "padding", "5px 20px", "margin", "0", "color", "#bb0919", "font-weight", "700", "font-size", "1.6em"], ["mat-table", "", "matSort", "", "matSortActive", "percent", "matSortDisableClear", "", "matSortDirection", "desc", 1, "mat-elevation-z8", "w-100", "font-bold", 3, "dataSource"], ["matColumnDef", "pair"], ["mat-header-cell", "", 4, "matHeaderCellDef"], ["mat-cell", "", 4, "matCellDef"], ["matColumnDef", "buy"], ["mat-cell", "", "class", "cursor-pointer", 3, "click", 4, "matCellDef"], ["matColumnDef", "sell"], ["matColumnDef", "percent"], ["mat-header-row", "", 4, "matHeaderRowDef"], ["mat-row", "", 3, "ngStyle", 4, "matRowDef", "matRowDefColumns"], ["class", "mat-row", 4, "matNoDataRow"], [3, "notices", "interval", "timer", "pushKoef"], ["mat-header-cell", ""], ["mat-cell", ""], ["mat-icon-button", "", "aria-label", "hide-pair", 1, "cursor-pointer", 3, "click"], [1, "font-lighter"], ["mat-cell", "", 1, "cursor-pointer", 3, "click"], [4, "ngIf"], ["mat-header-row", ""], ["mat-row", "", 3, "ngStyle"], [1, "mat-row"], ["colspan", "4", 1, "mat-cell"]], template: function MainTableComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "app-socket", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-form-field");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "mat-label");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Filter");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "input", 1, 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup", function MainTableComponent_Template_input_keyup_4_listener($event) { return ctx.applyFilter($event); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "h3", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "table", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](9, 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](10, MainTableComponent_th_10_Template, 2, 0, "th", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](11, MainTableComponent_td_11_Template, 5, 1, "td", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](12, 8);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](13, MainTableComponent_th_13_Template, 2, 0, "th", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](14, MainTableComponent_td_14_Template, 3, 3, "td", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](15, 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](16, MainTableComponent_th_16_Template, 2, 0, "th", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](17, MainTableComponent_td_17_Template, 3, 4, "td", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](18, 11);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](19, MainTableComponent_th_19_Template, 2, 0, "th", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](20, MainTableComponent_td_20_Template, 2, 1, "td", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](21, MainTableComponent_tr_21_Template, 1, 0, "tr", 12);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](22, MainTableComponent_tr_22_Template, 1, 3, "tr", 13);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](23, MainTableComponent_tr_23_Template, 3, 1, "tr", 14);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](24, "app-notice", 15);
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("API_KEYS", ctx.apiKeys)("tokenPrices", ctx.tokenPrices);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate2"]("Normal: ", ctx.gasNormal, " | Fast ", ctx.gasFast, "");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("dataSource", ctx.dataSource);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](13);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matHeaderRowDef", ctx.displayedColumns);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matRowDefColumns", ctx.displayedColumns);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("notices", ctx.notices)("interval", ctx.noticesTimer)("timer", ctx.timer)("pushKoef", ctx.pushKoef);
    } }, directives: [_socket_socket_component__WEBPACK_IMPORTED_MODULE_3__["SocketComponent"], _angular_material_form_field__WEBPACK_IMPORTED_MODULE_4__["MatFormField"], _angular_material_form_field__WEBPACK_IMPORTED_MODULE_4__["MatLabel"], _angular_material_input__WEBPACK_IMPORTED_MODULE_5__["MatInput"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatTable"], _angular_material_sort__WEBPACK_IMPORTED_MODULE_6__["MatSort"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatColumnDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatNoDataRow"], _notice_notice_component__WEBPACK_IMPORTED_MODULE_7__["NoticeComponent"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderCell"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatCell"], _angular_material_button__WEBPACK_IMPORTED_MODULE_8__["MatButton"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_9__["MatIcon"], _angular_common__WEBPACK_IMPORTED_MODULE_10__["NgIf"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatHeaderRow"], _angular_material_table__WEBPACK_IMPORTED_MODULE_1__["MatRow"], _angular_common__WEBPACK_IMPORTED_MODULE_10__["NgStyle"]], styles: ["table[_ngcontent-%COMP%]   tr[_ngcontent-%COMP%]:nth-child(even) {\r\n  border: 4px solid #000000 !important;\r\n  box-shadow: inset 2000px 0 0 0 rgba(0, 0, 0, 0.2);\r\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvY29tcG9uZW50cy9tYWluLXRhYmxlL21haW4tdGFibGUuY29tcG9uZW50LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtFQUNFLG9DQUFvQztFQUNwQyxpREFBaUQ7QUFDbkQiLCJmaWxlIjoic3JjL2FwcC9jb21wb25lbnRzL21haW4tdGFibGUvbWFpbi10YWJsZS5jb21wb25lbnQuY3NzIiwic291cmNlc0NvbnRlbnQiOlsidGFibGUgdHI6bnRoLWNoaWxkKGV2ZW4pIHtcclxuICBib3JkZXI6IDRweCBzb2xpZCAjMDAwMDAwICFpbXBvcnRhbnQ7XHJcbiAgYm94LXNoYWRvdzogaW5zZXQgMjAwMHB4IDAgMCAwIHJnYmEoMCwgMCwgMCwgMC4yKTtcclxufVxyXG4iXX0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](MainTableComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-main-table',
                templateUrl: './main-table.component.html',
                styleUrls: ['./main-table.component.css']
            }]
    }], function () { return [{ type: _services_api_service_service__WEBPACK_IMPORTED_MODULE_2__["ApiServiceService"] }, { type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgZone"] }]; }, null); })();


/***/ }),

/***/ "2MiI":
/*!*******************************************************!*\
  !*** ./src/app/components/header/header.component.ts ***!
  \*******************************************************/
/*! exports provided: HeaderComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HeaderComponent", function() { return HeaderComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");


class HeaderComponent {
    constructor() { }
    ngOnInit() {
    }
}
HeaderComponent.ɵfac = function HeaderComponent_Factory(t) { return new (t || HeaderComponent)(); };
HeaderComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: HeaderComponent, selectors: [["app-header"]], decls: 0, vars: 0, template: function HeaderComponent_Template(rf, ctx) { }, styles: [".spacer[_ngcontent-%COMP%] {\r\n  flex: 1 1 auto;\r\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvY29tcG9uZW50cy9oZWFkZXIvaGVhZGVyLmNvbXBvbmVudC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFDRSxjQUFjO0FBQ2hCIiwiZmlsZSI6InNyYy9hcHAvY29tcG9uZW50cy9oZWFkZXIvaGVhZGVyLmNvbXBvbmVudC5jc3MiLCJzb3VyY2VzQ29udGVudCI6WyIuc3BhY2VyIHtcclxuICBmbGV4OiAxIDEgYXV0bztcclxufVxyXG4iXX0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](HeaderComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-header',
                templateUrl: './header.component.html',
                styleUrls: ['./header.component.css']
            }]
    }], function () { return []; }, null); })();


/***/ }),

/***/ "AytR":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
const environment = {
    production: false,
    Idex_WSS_URL: 'wss://datastream.idex.market',
    Idex_API_KEY: 'cddba27a-916f-48e7-bad3-884c0869b627',
    Idex_API_Secret: 'phqt5YCeyWym5cfShzsw6YCL9uL9hoPo',
    // Binance
    Binance_WSS_URL: 'wss://stream.binance.com:9443',
    Binance_API_KEY: 'XpmQTvaLsmvEaK7Y53ms8Z8HhuqQLFwcMfb46bzKk43zzFnhvj0DUcGrOl9VJWsS',
    Binance_API_Secret: 'Bhte5kVRDKgSu4ZJPthFzF2nlByI1i5qHddwGF63W0Ad70NgHSdpBkggdYXNwOLC',
    // huobi.com
    Huobi_WSS_URL: 'wss://api.huobi.pro/ws',
    Huobi_API_KEY: '019d0c05-5ab68c59-bgbfh5tv3f-3786b',
    Huobi_API_Secret: '76054023-a15f7e50-c38931ef-98b2a',
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "F5WS":
/*!*******************************************************!*\
  !*** ./src/app/components/socket/socket.component.ts ***!
  \*******************************************************/
/*! exports provided: SocketComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SocketComponent", function() { return SocketComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! rxjs */ "qCKp");
/* harmony import */ var _services_api_service_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../services/api-service.service */ "ul72");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/common */ "ofXK");





function SocketComponent_ng_container_3_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const message_r2 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", message_r2, " ");
} }
function SocketComponent_ng_container_4_p_1_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 5);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "a", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "a", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "span", 7);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const message_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", message_r3.percent > 2 ? "log_msg log_sell red" : "log_msg log_sell");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", message_r3["time"], " - \u041F\u0440\u043E\u0434\u0430\u0436\u0430 - \u0446\u0435\u043D\u0430 c IDEX: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("href", message_r3.urlbuy, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](message_r3.iprice);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" -> \u0446\u0435\u043D\u0430 \u043D\u0430 ", message_r3.market, ": ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("href", message_r3.urlsell, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", message_r3.price, "");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" = ", message_r3.token, " ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", message_r3.percent, "%");
} }
function SocketComponent_ng_container_4_p_2_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 8);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "span", 7);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const message_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate5"](" ", message_r3["time"], " - \u041F\u043E\u043A\u0443\u043F\u043A\u0430 - \u0446\u0435\u043D\u0430 \u0441 IDEX: ", message_r3.iprice, " -> \u0446\u0435\u043D\u0430 \u043D\u0430 ", message_r3.market, ": ", message_r3.price, " = ", message_r3.token, " ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", message_r3.percent, "%");
} }
function SocketComponent_ng_container_4_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](1, SocketComponent_ng_container_4_p_1_Template, 10, 9, "p", 3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, SocketComponent_ng_container_4_p_2_Template, 4, 6, "p", 4);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const message_r3 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", message_r3.type === "buy");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", message_r3.type === "sell");
} }
let tokenPrice = [];
const socketMsgs = [];
const socketStatuses = [];
class SocketComponent {
    constructor(api) {
        this.api = api;
        this.API_KEYS = [];
        this.tokenPrices = [];
        this.socketMsg = socketMsgs;
        this.socketStatus = socketStatuses;
        this.playAlarm = () => {
            // const audio = new Audio();
            // audio.src = '../../../assets/beep-4.mp3';
            // audio.load();
            // audio.volume = 0.2;
            // audio.play();
        };
        // console.log(await publicClient.getServerTime());
        this.isShowing = false;
        this.api.getPublicApi('https://api.idex.io/v1/markets').subscribe((result) => {
            const tokens = [];
            result.forEach((res) => {
                tokens.push(res.market);
            });
            this.connect(tokens);
            tokenPrice = this.tokenPrices;
        });
    }
    // tslint:disable-next-line:typedef
    ngOnChanges(changes) {
        // tslint:disable-next-line:forin
        for (const propName in changes) {
            if (propName === 'tokenPrices') {
                tokenPrice = changes[propName].currentValue;
                if (tokenPrice.length > 0 && !this.isShowing) {
                    this.showLog();
                    this.isShowing = true;
                }
            }
        }
    }
    connect(tokens) {
        const wss = new WebSocket('wss://websocket.idex.io/v1');
        wss.onopen = (event) => {
            this.wssIsAlive = true;
            this.subscribe(wss, tokens);
        };
        wss.onmessage = (event) => {
            const sdata = JSON.parse(event.data);
            if (sdata.subscriptions) {
                // console.log(sdata.subscriptions);
            }
            else {
                console.log(sdata.type, sdata);
                setTimeout(() => {
                    this.getComparToket(sdata.data).subscribe(res => {
                        this.socketMsg.unshift(res);
                    });
                }, 10);
                // const logData = JSON.stringify(sdata);
                // this.api.postApi('websocket_log/', {log: logData}).subscribe((res: any[]) => {
                //   console.log(res);
                // });
            }
        };
        wss.onerror = (err) => {
            console.error('Socket encountered error: ', err, 'Closing socket');
            wss.close();
        };
        wss.onerror = (event) => {
            console.error('WebSocket error observed:', event);
        };
        wss.onclose = (e) => {
            console.log('Close', e);
            console.log('Try reconnect', e);
            setTimeout(() => {
                this.connect(tokens);
            }, 1000);
        };
        // setInterval(() => {
        //   wss.send(JSON.stringify({type: 'ping', data: {}}));
        // }, 1000);
    }
    subscribe(wss, tokens) {
        const message = {
            method: 'subscribe',
            markets: tokens,
            subscriptions: [
                // 'tickers',
                'trades',
            ]
        };
        wss.send(JSON.stringify(message));
    }
    getComparToket(trade) {
        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])(this.comparToken(trade));
    }
    comparToken(trade) {
        console.log(trade);
        const data = [];
        this.lastEvent = trade;
        tokenPrice.forEach(token => {
            if (token.exch_direction.toLowerCase() === trade.m.replace('-ETH', '').toLowerCase()) {
                const tradePrice = parseFloat(trade.p);
                if (token.site === 'kyber') {
                    data.push({
                        time: new Date(trade.t).toLocaleString(),
                        type: trade.s,
                        market: 'Kyber',
                        token: trade.m.replace('-ETH', ''),
                        iprice: tradePrice,
                        price: token.sell,
                        percent: Number((token.sell - tradePrice) / (tradePrice / 100)).toFixed(2),
                        urlbuy: 'https://exchange.idex.io/trading/' + trade.m.replace('-ETH', '') + '-ETH',
                        urlsell: 'https://kyberswap.com/swap/ent-' + trade.m.replace('-ETH', '').toLowerCase()
                    });
                }
                if (token.site === 'bancor') {
                    data.push({
                        time: new Date(trade.t).toLocaleString(),
                        type: trade.s,
                        market: 'Bankor',
                        token: trade.m.replace('-ETH', ''),
                        iprice: tradePrice,
                        price: token.sell,
                        percent: Number((token.sell - tradePrice) / (tradePrice / 100)).toFixed(2),
                        urlbuy: 'https://exchange.idex.io/trading/' + trade.m.replace('-ETH', '') + '-ETH',
                        urlsell: 'https://www.bancor.network/?q=' + trade.m.replace('-ETH', '').toLowerCase()
                    });
                }
                // if (token.uniswaponebid) {
                //   data.push({
                //     time: new Date(trade.t).toLocaleString(),
                //     type: trade.s,
                //     market: 'Uniswap_V1',
                //     token: trade.m.replace('-ETH', ''),
                //     iprice: tradePrice,
                //     price: token.sell,
                //     percent: Number((token.sell - tradePrice) / (tradePrice / 100)).toFixed(2),
                //     urlbuy: 'https://exchange.idex.io/trading/' + trade.m.replace('-ETH', '') + '-ETH',
                //     urlsell: 'https://app.uniswap.org/#/swap?outputCurrency=' + token.uniswaponeid + '&use=v1'
                //   });
                // }
                if (token.site === 'uniswap') {
                    data.push({
                        time: new Date(trade.t).toLocaleString(),
                        type: trade.s,
                        market: 'Uniswap_V2',
                        token: trade.m.replace('-ETH', ''),
                        iprice: tradePrice,
                        price: token.sell,
                        percent: Number((token.sell - tradePrice) / (tradePrice / 100)).toFixed(2),
                        urlbuy: 'https://exchange.idex.io/trading/' + trade.m.replace('-ETH', '') + '-ETH',
                        urlsell: 'https://app.uniswap.org/#/swap?outputCurrency=' + token.contract
                    });
                }
                if (trade.s === 'buy') {
                    this.playAlarm();
                }
            }
        });
        return data;
    }
    showLog() {
        this.api.getApi('websocket_log/').subscribe((res) => {
            res.forEach(elem => {
                const result = {
                    time: new Date(elem.datetime).toLocaleString(),
                    type: elem.type,
                    market: elem.site,
                    token: elem.token,
                    iprice: elem.price,
                    price: elem.sprice,
                    percent: elem.percent,
                    urlbuy: elem.buy_url,
                    urlsell: elem.sell_url
                };
                this.socketMsg.push(result);
            });
        });
    }
}
SocketComponent.ɵfac = function SocketComponent_Factory(t) { return new (t || SocketComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_api_service_service__WEBPACK_IMPORTED_MODULE_2__["ApiServiceService"])); };
SocketComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: SocketComponent, selectors: [["app-socket"]], inputs: { API_KEYS: "API_KEYS", tokenPrices: "tokenPrices" }, features: [_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵNgOnChangesFeature"]], decls: 5, vars: 2, consts: [["id", "socket_log", 1, "socket_log"], [1, "w_title"], [4, "ngFor", "ngForOf"], [3, "ngClass", 4, "ngIf"], ["class", "log_msg log_buy", 4, "ngIf"], [3, "ngClass"], ["target", "_blank", 3, "href"], [1, "percent"], [1, "log_msg", "log_buy"]], template: function SocketComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "h4", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "WebSocket: ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](3, SocketComponent_ng_container_3_Template, 2, 1, "ng-container", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](4, SocketComponent_ng_container_4_Template, 3, 2, "ng-container", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.socketStatus);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.socketMsg);
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_3__["NgForOf"], _angular_common__WEBPACK_IMPORTED_MODULE_3__["NgIf"], _angular_common__WEBPACK_IMPORTED_MODULE_3__["NgClass"]], styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvc29ja2V0L3NvY2tldC5jb21wb25lbnQuY3NzIn0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SocketComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-socket',
                templateUrl: './socket.component.html',
                styleUrls: ['./socket.component.css']
            }]
    }], function () { return [{ type: _services_api_service_service__WEBPACK_IMPORTED_MODULE_2__["ApiServiceService"] }]; }, { API_KEYS: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }], tokenPrices: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }] }); })();


/***/ }),

/***/ "Hiz6":
/*!*******************************************************!*\
  !*** ./src/app/components/hotbit/hotbit.component.ts ***!
  \*******************************************************/
/*! exports provided: HotbitComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HotbitComponent", function() { return HotbitComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _services_hotbit_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../services/hotbit.service */ "xV9Y");



class HotbitComponent {
    constructor(hotbit) {
        this.hotbit = hotbit;
        this.init = () => {
            // this.hotbit.getProfits().then((value) => {
            //   this.profits = value;
            //   console.log(this.profits);
            // });
        };
    }
    ngOnInit() {
        this.init();
    }
}
HotbitComponent.ɵfac = function HotbitComponent_Factory(t) { return new (t || HotbitComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_hotbit_service__WEBPACK_IMPORTED_MODULE_1__["HotbitService"])); };
HotbitComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: HotbitComponent, selectors: [["app-hotbit"]], decls: 2, vars: 0, template: function HotbitComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, "hotbit works!");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } }, styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvaG90Yml0L2hvdGJpdC5jb21wb25lbnQuY3NzIn0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](HotbitComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-hotbit',
                templateUrl: './hotbit.component.html',
                styleUrls: ['./hotbit.component.css']
            }]
    }], function () { return [{ type: _services_hotbit_service__WEBPACK_IMPORTED_MODULE_1__["HotbitService"] }]; }, null); })();


/***/ }),

/***/ "Sy1n":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _components_header_header_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./components/header/header.component */ "2MiI");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _components_foot_foot_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/foot/foot.component */ "ZYbi");





class AppComponent {
    constructor() {
        this.title = 'excomparison';
    }
}
AppComponent.ɵfac = function AppComponent_Factory(t) { return new (t || AppComponent)(); };
AppComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: AppComponent, selectors: [["app-root"]], decls: 3, vars: 0, consts: [[1, "w-100"]], template: function AppComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "app-header", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "router-outlet", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](2, "app-foot", 0);
    } }, directives: [_components_header_header_component__WEBPACK_IMPORTED_MODULE_1__["HeaderComponent"], _angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterOutlet"], _components_foot_foot_component__WEBPACK_IMPORTED_MODULE_3__["FootComponent"]], styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2FwcC5jb21wb25lbnQuY3NzIn0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AppComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-root',
                templateUrl: './app.component.html',
                styleUrls: ['./app.component.css']
            }]
    }], null, null); })();


/***/ }),

/***/ "ZAI4":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "jhN1");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app.component */ "Sy1n");
/* harmony import */ var _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/main-table/main-table.component */ "0d3g");
/* harmony import */ var _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/platform-browser/animations */ "R1ws");
/* harmony import */ var _components_header_header_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./components/header/header.component */ "2MiI");
/* harmony import */ var _components_foot_foot_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./components/foot/foot.component */ "ZYbi");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _angular_material_menu__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @angular/material/menu */ "STbY");
/* harmony import */ var _angular_material_button__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @angular/material/button */ "bTqV");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @angular/common/http */ "tk/3");
/* harmony import */ var _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @angular/material/grid-list */ "zkoq");
/* harmony import */ var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @angular/material/toolbar */ "/t3+");
/* harmony import */ var _angular_material_icon__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @angular/material/icon */ "NFeN");
/* harmony import */ var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @angular/material/form-field */ "kmnG");
/* harmony import */ var _angular_material_input__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @angular/material/input */ "qFsG");
/* harmony import */ var _angular_material_table__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @angular/material/table */ "+0xr");
/* harmony import */ var _components_notice_notice_component__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ./components/notice/notice.component */ "dlut");
/* harmony import */ var _angular_material_sort__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! @angular/material/sort */ "Dh3D");
/* harmony import */ var _components_socket_socket_component__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! ./components/socket/socket.component */ "F5WS");
/* harmony import */ var _components_hotbit_hotbit_component__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! ./components/hotbit/hotbit.component */ "Hiz6");























class AppModule {
}
AppModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({ type: AppModule, bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"]] });
AppModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({ factory: function AppModule_Factory(t) { return new (t || AppModule)(); }, providers: [], imports: [[
            _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
            _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_4__["BrowserAnimationsModule"],
            _angular_common_http__WEBPACK_IMPORTED_MODULE_10__["HttpClientModule"],
            _angular_router__WEBPACK_IMPORTED_MODULE_7__["RouterModule"].forRoot([
                { path: '', component: _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__["MainTableComponent"] },
                { path: 'main', component: _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__["MainTableComponent"] },
            ]),
            _angular_material_menu__WEBPACK_IMPORTED_MODULE_8__["MatMenuModule"],
            _angular_material_button__WEBPACK_IMPORTED_MODULE_9__["MatButtonModule"],
            _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__["MatGridListModule"],
            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_12__["MatToolbarModule"],
            _angular_material_icon__WEBPACK_IMPORTED_MODULE_13__["MatIconModule"],
            _angular_material_form_field__WEBPACK_IMPORTED_MODULE_14__["MatFormFieldModule"],
            _angular_material_input__WEBPACK_IMPORTED_MODULE_15__["MatInputModule"],
            _angular_material_table__WEBPACK_IMPORTED_MODULE_16__["MatTableModule"],
            _angular_material_sort__WEBPACK_IMPORTED_MODULE_18__["MatSortModule"],
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](AppModule, { declarations: [_app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"],
        _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__["MainTableComponent"],
        _components_header_header_component__WEBPACK_IMPORTED_MODULE_5__["HeaderComponent"],
        _components_foot_foot_component__WEBPACK_IMPORTED_MODULE_6__["FootComponent"],
        _components_notice_notice_component__WEBPACK_IMPORTED_MODULE_17__["NoticeComponent"],
        _components_socket_socket_component__WEBPACK_IMPORTED_MODULE_19__["SocketComponent"],
        _components_hotbit_hotbit_component__WEBPACK_IMPORTED_MODULE_20__["HotbitComponent"]], imports: [_angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
        _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_4__["BrowserAnimationsModule"],
        _angular_common_http__WEBPACK_IMPORTED_MODULE_10__["HttpClientModule"], _angular_router__WEBPACK_IMPORTED_MODULE_7__["RouterModule"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_8__["MatMenuModule"],
        _angular_material_button__WEBPACK_IMPORTED_MODULE_9__["MatButtonModule"],
        _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__["MatGridListModule"],
        _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_12__["MatToolbarModule"],
        _angular_material_icon__WEBPACK_IMPORTED_MODULE_13__["MatIconModule"],
        _angular_material_form_field__WEBPACK_IMPORTED_MODULE_14__["MatFormFieldModule"],
        _angular_material_input__WEBPACK_IMPORTED_MODULE_15__["MatInputModule"],
        _angular_material_table__WEBPACK_IMPORTED_MODULE_16__["MatTableModule"],
        _angular_material_sort__WEBPACK_IMPORTED_MODULE_18__["MatSortModule"]] }); })();
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](AppModule, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
        args: [{
                declarations: [
                    _app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"],
                    _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__["MainTableComponent"],
                    _components_header_header_component__WEBPACK_IMPORTED_MODULE_5__["HeaderComponent"],
                    _components_foot_foot_component__WEBPACK_IMPORTED_MODULE_6__["FootComponent"],
                    _components_notice_notice_component__WEBPACK_IMPORTED_MODULE_17__["NoticeComponent"],
                    _components_socket_socket_component__WEBPACK_IMPORTED_MODULE_19__["SocketComponent"],
                    _components_hotbit_hotbit_component__WEBPACK_IMPORTED_MODULE_20__["HotbitComponent"],
                ],
                imports: [
                    _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                    _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_4__["BrowserAnimationsModule"],
                    _angular_common_http__WEBPACK_IMPORTED_MODULE_10__["HttpClientModule"],
                    _angular_router__WEBPACK_IMPORTED_MODULE_7__["RouterModule"].forRoot([
                        { path: '', component: _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__["MainTableComponent"] },
                        { path: 'main', component: _components_main_table_main_table_component__WEBPACK_IMPORTED_MODULE_3__["MainTableComponent"] },
                    ]),
                    _angular_material_menu__WEBPACK_IMPORTED_MODULE_8__["MatMenuModule"],
                    _angular_material_button__WEBPACK_IMPORTED_MODULE_9__["MatButtonModule"],
                    _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__["MatGridListModule"],
                    _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_12__["MatToolbarModule"],
                    _angular_material_icon__WEBPACK_IMPORTED_MODULE_13__["MatIconModule"],
                    _angular_material_form_field__WEBPACK_IMPORTED_MODULE_14__["MatFormFieldModule"],
                    _angular_material_input__WEBPACK_IMPORTED_MODULE_15__["MatInputModule"],
                    _angular_material_table__WEBPACK_IMPORTED_MODULE_16__["MatTableModule"],
                    _angular_material_sort__WEBPACK_IMPORTED_MODULE_18__["MatSortModule"],
                ],
                providers: [],
                bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"]]
            }]
    }], null, null); })();


/***/ }),

/***/ "ZYbi":
/*!***************************************************!*\
  !*** ./src/app/components/foot/foot.component.ts ***!
  \***************************************************/
/*! exports provided: FootComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FootComponent", function() { return FootComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");


class FootComponent {
    constructor() { }
    ngOnInit() {
    }
}
FootComponent.ɵfac = function FootComponent_Factory(t) { return new (t || FootComponent)(); };
FootComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: FootComponent, selectors: [["app-foot"]], decls: 2, vars: 0, consts: [[1, "w-100"]], template: function FootComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "hr");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } }, styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvZm9vdC9mb290LmNvbXBvbmVudC5jc3MifQ== */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](FootComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-foot',
                templateUrl: './foot.component.html',
                styleUrls: ['./foot.component.css']
            }]
    }], function () { return []; }, null); })();


/***/ }),

/***/ "dlut":
/*!*******************************************************!*\
  !*** ./src/app/components/notice/notice.component.ts ***!
  \*******************************************************/
/*! exports provided: NoticeComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "NoticeComponent", function() { return NoticeComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "ofXK");



const _c0 = ["noticeArea"];
const _c1 = function (a0) { return { "show": a0 }; };
class NoticeComponent {
    constructor(renderer) {
        this.renderer = renderer;
        this.notices = [];
        this.timer = 2000;
        this.interval = 10;
        this.pushKoef = 1;
        this.allNotices = [];
        this.isShow = false;
        this.changelog = [];
        this.setNotice = () => {
            if (!this.isShow) {
                this.isShow = this.notices.length > 0;
            }
            if (this.allNotices.length > 0) {
                this.notices.forEach((elem) => {
                    let equal = false;
                    let idx = null;
                    this.allNotices.forEach((el, index) => {
                        if (elem.pair === el.pair) {
                            equal = true;
                            idx = index;
                        }
                    });
                    if (equal) {
                        const kef = elem.percent - (this.allNotices[idx].percent + this.pushKoef);
                        if (kef > this.pushKoef) {
                            this.showNotice(elem);
                        }
                        // this.allNotices[idx].percent = elem.persent;
                    }
                    else {
                        this.showNotice(elem);
                        this.allNotices.push(elem);
                    }
                });
            }
            else {
                this.notices.forEach((el) => {
                    this.allNotices.push(el);
                    this.showNotice(el);
                });
            }
        };
        this.showNotice = (notice) => {
            const p = this.renderer.createElement('p');
            p.className = 'pnotice';
            p.setAttribute('aria-label', this.interval.toString());
            p.innerHTML = notice.pair + '<a href="' + notice.buyurl + '" target="_blank">С ' + notice.buy_name + '</a>' + ' за ' +
                ' на ' + '<a href="' + notice.sellurl + '" target="_blank">' + notice.sell_name + '</a>' + ' ~ ' + notice.percent + '%';
            this.renderer.appendChild(this.noticeArea.nativeElement, p);
            this.playAlarm();
        };
        this.checkNotice = () => {
            const elements = Array.from(document.getElementsByClassName('pnotice'));
            if (elements.length > 0) {
                for (const el of elements) {
                    const t = parseInt(el.getAttribute('aria-label'), 10);
                    if (t === 0) {
                        el.remove();
                    }
                    else {
                        el.setAttribute('aria-label', (t - 1).toString());
                    }
                }
            }
        };
        this.playAlarm = () => {
            const audio = new Audio();
            audio.src = '../../../assets/alarm.wav';
            audio.load();
            audio.volume = 0.2;
            audio.play();
        };
        setInterval(() => {
            this.checkNotice();
        }, 1000);
    }
    // tslint:disable-next-line:typedef
    ngOnChanges(changes) {
        // tslint:disable-next-line:forin
        for (const propName in changes) {
            if (propName === 'notices') {
                this.notices = changes[propName].currentValue;
                this.setNotice();
            }
        }
    }
}
NoticeComponent.ɵfac = function NoticeComponent_Factory(t) { return new (t || NoticeComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["Renderer2"])); };
NoticeComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: NoticeComponent, selectors: [["app-notice"]], viewQuery: function NoticeComponent_Query(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵviewQuery"](_c0, true);
    } if (rf & 2) {
        var _t;
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵloadQuery"]()) && (ctx.noticeArea = _t.first);
    } }, inputs: { notices: "notices", timer: "timer", interval: "interval", pushKoef: "pushKoef" }, features: [_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵNgOnChangesFeature"]], decls: 2, vars: 3, consts: [["id", "notify-container", 3, "ngClass"], ["noticeArea", ""]], template: function NoticeComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "div", 0, 1);
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction1"](1, _c1, ctx.isShow));
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["NgClass"]], styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvbm90aWNlL25vdGljZS5jb21wb25lbnQuY3NzIn0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](NoticeComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-notice',
                templateUrl: './notice.component.html',
                styleUrls: ['./notice.component.css']
            }]
    }], function () { return [{ type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Renderer2"] }]; }, { notices: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }], timer: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }], interval: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }], pushKoef: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }], noticeArea: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewChild"],
            args: ['noticeArea']
        }] }); })();


/***/ }),

/***/ "ul72":
/*!*************************************************!*\
  !*** ./src/app/services/api-service.service.ts ***!
  \*************************************************/
/*! exports provided: ApiServiceService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ApiServiceService", function() { return ApiServiceService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "tk/3");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs */ "qCKp");
/* harmony import */ var rxjs_operators__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! rxjs/operators */ "kU1M");






class ApiServiceService {
    constructor(http) {
        this.http = http;
        // apiUrl = 'http://dev.xc.vp4.ru/';
        this.apiUrl = 'http://xc.vp4.ru/';
        // apiUrl = 'http://127.0.0.1:8000/';
        this.headers = new _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpHeaders"]();
        this.headersPub = new _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpHeaders"]();
        this.token = 'fZZ5mwam.UkBnR1iAHhK81HcZFxufRKhQrWDB1inL';
        this.setHeaders = () => {
            this.headersPub = this.headers.set('Content-Type', 'application/json');
            this.headers = this.headers.set('Content-Type', 'application/json');
            if (this.token) {
                this.headers = this.headers.set('X-Api-Key', this.token);
            }
        };
        // Handle Errors
        this.error = (error) => {
            let errorMessage = '';
            if (error.error instanceof ErrorEvent) {
                errorMessage = error.error.message;
            }
            else {
                errorMessage = `${error.error.error}`;
            }
            return Object(rxjs__WEBPACK_IMPORTED_MODULE_2__["throwError"])(errorMessage);
        };
        this.setHeaders();
    }
    getPublicApi(url) {
        return this.http.get(url, { headers: this.headersPub }).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_3__["catchError"])(this.error));
    }
    getApi(url) {
        return this.http.get(this.apiUrl + url, { headers: this.headers }).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_3__["catchError"])(this.error));
    }
    postApi(url, body) {
        return this.http.post(this.apiUrl + url, body, { headers: this.headers }).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_3__["catchError"])(this.error));
    }
}
ApiServiceService.ɵfac = function ApiServiceService_Factory(t) { return new (t || ApiServiceService)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵinject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"])); };
ApiServiceService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: ApiServiceService, factory: ApiServiceService.ɵfac, providedIn: 'root' });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](ApiServiceService, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
        args: [{
                providedIn: 'root'
            }]
    }], function () { return [{ type: _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"] }]; }, null); })();


/***/ }),

/***/ "xV9Y":
/*!********************************************!*\
  !*** ./src/app/services/hotbit.service.ts ***!
  \********************************************/
/*! exports provided: HotbitService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HotbitService", function() { return HotbitService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "tk/3");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs */ "qCKp");
/* harmony import */ var _api_service_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./api-service.service */ "ul72");






class HotbitService {
    constructor(http, api) {
        this.http = http;
        this.api = api;
        this.apiUrl = 'http://127.0.0.1:8000/hotbitv/';
        this.headers = new _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpHeaders"]();
        this.headersPub = new _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpHeaders"]();
        this.token = 'fZZ5mwam.UkBnR1iAHhK81HcZFxufRKhQrWDB1inL';
        this.setHeaders = () => {
            this.headersPub = this.headers.set('Content-Type', 'application/json');
            this.headersPub = this.headers.set('Access-Control-Allow-Origin', '*');
            this.headersPub = this.headers.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
            this.headers = this.headers.set('Content-Type', 'application/json');
            if (this.token) {
                this.headers = this.headers.set('X-Api-Key', this.token);
            }
        };
        this.getProfits = () => {
            this.api.postApi('hotbitv/', {}).subscribe(res => { console.log(res); });
        };
        // Handle Errors
        this.error = (error) => {
            let errorMessage = '';
            if (error.error instanceof ErrorEvent) {
                errorMessage = error.error.message;
            }
            else {
                errorMessage = `${error.error.error}`;
            }
            return Object(rxjs__WEBPACK_IMPORTED_MODULE_2__["throwError"])(errorMessage);
        };
        this.setHeaders();
    }
}
HotbitService.ɵfac = function HotbitService_Factory(t) { return new (t || HotbitService)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵinject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵinject"](_api_service_service__WEBPACK_IMPORTED_MODULE_3__["ApiServiceService"])); };
HotbitService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: HotbitService, factory: HotbitService.ɵfac, providedIn: 'root' });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](HotbitService, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
        args: [{
                providedIn: 'root'
            }]
    }], function () { return [{ type: _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"] }, { type: _api_service_service__WEBPACK_IMPORTED_MODULE_3__["ApiServiceService"] }]; }, null); })();


/***/ }),

/***/ "zUnb":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./environments/environment */ "AytR");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "ZAI4");
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/platform-browser */ "jhN1");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_1__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
_angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__["platformBrowser"]().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(err => console.error(err));


/***/ }),

/***/ "zn8P":
/*!******************************************************!*\
  !*** ./$$_lazy_route_resource lazy namespace object ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "zn8P";

/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map